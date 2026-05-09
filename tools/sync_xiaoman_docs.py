#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import hashlib
import html as html_lib
import json
import os
import re
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
LLMS_URL = "https://open.xiaoman.cn/llms.txt"
DEFAULT_SERVER = "https://api-sandbox.xiaoman.cn"
HTTP_METHODS = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}
IMAGE_EXTENSIONS = {
    "image/jpeg": ".jpeg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
}
LOCALIZABLE_SOURCE_RE = re.compile(r"(api-\d+|doc-\d+|folder-\d+|schema-\d+)")
MARKDOWN_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\((https?://[^\s)]+)(\s+(?:\"[^\"]*\"|'[^']*'))?\)")

MODULE_SLUGS = {
    "授权登录": "auth",
    "客户": "company",
    "销售订单": "sales-order",
    "采购订单": "purchase-order",
    "产品": "product",
    "回款登记": "receipt-registration",
    "回款单": "receipt",
    "付款单": "payment",
    "费用单": "cost-invoice",
    "报价单": "quotation",
    "供应商": "supplier",
    "商机": "opportunity",
    "用户": "user",
    "销售出库单": "sales-outbound",
    "库存": "warehouse",
    "线索": "lead",
    "资金": "capital-account",
    "采购入库单": "purchase-inbound",
    "采购退货单": "purchase-return",
    "示例接口（勿用）": "example-do-not-use",
    "消息推送": "webhook",
    "统计分析": "analytics",
    "devops相关": "devops",
    "WhatsApp": "whatsapp",
    "未分组": "unassigned",
}


@dataclasses.dataclass(frozen=True)
class CatalogEntry:
    section: str
    module: str
    title: str
    url: str
    description: str
    kind: str
    source_id: str
    source_file: str
    module_slug: str


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def module_slug(module: str) -> str:
    if module in MODULE_SLUGS:
        return MODULE_SLUGS[module]
    digest = hashlib.sha1(module.encode("utf-8")).hexdigest()[:8]
    return f"module-{digest}"


def source_id_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    return Path(path).stem


def source_file_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    name = Path(path).name
    if not name.endswith(".md"):
        name = f"{Path(path).stem}.md"
    return name


def kind_from_source_id(source_id: str) -> str:
    if source_id.startswith("api-"):
        return "api"
    if source_id.startswith("folder-"):
        return "folder"
    return "doc"


def fetch_text(url: str, retries: int = 3) -> str:
    headers = {
        "User-Agent": "xiaoman-openapi-sync/0.1 (+https://github.com/frankie0736/xiaoman-openapi)",
        "Accept": "text/markdown,text/plain,*/*",
    }
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=30) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def fetch_bytes(url: str, retries: int = 3) -> tuple[bytes, str]:
    headers = {
        "User-Agent": "xiaoman-openapi-sync/0.1 (+https://github.com/frankie0736/xiaoman-openapi)",
        "Accept": "*/*",
    }
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read(), response.headers.get_content_type()
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def redact_text(text: str) -> str:
    replacements = [
        (r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "REDACTED_JWT"),
        (r"biai-whatsapp-[A-Za-z0-9_-]{16,}", "biai-whatsapp-REDACTED"),
        (r"(?i)(client_secret\s*[:=]\s*[\"']?)[A-Za-z0-9_-]{16,}", r"\1REDACTED_CLIENT_SECRET"),
        (r"(?i)(secretKey\s*=\s*[\"'])[A-Za-z0-9+/=]{24,}([\"'])", r"\1REDACTED_SECURITY_CONFIG\2"),
        (r"(?i)(signature\s*=\s*[\"'])[a-f0-9]{32,}([\"'])", r"\1REDACTED_SIGNATURE\2"),
        (r"(?i)(security_config[^\\n\"']{0,80}[\"'])[A-Za-z0-9+/=]{24,}([\"'])", r"\1REDACTED_SECURITY_CONFIG\2"),
        (r'("data"\s*:\s*")[A-Za-z0-9+/=]{60,}(")', r"\1REDACTED_ENCRYPTED_DATA\2"),
    ]
    redacted = text
    for pattern, replacement in replacements:
        redacted = re.sub(pattern, replacement, redacted)
    return redacted


def parse_catalog(llms_text: str) -> list[CatalogEntry]:
    entries: list[CatalogEntry] = []
    section = ""
    link_re = re.compile(
        r"^- (?:(?P<module>.+?) )?\[(?P<title>[^\]]+)\]\((?P<url>https?://[^)]+)\):\s*(?P<desc>.*)$"
    )
    for raw_line in llms_text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        match = link_re.match(line)
        if not match:
            continue
        title = match.group("title").strip()
        module = (match.group("module") or "").strip()
        url = match.group("url").strip()
        desc = match.group("desc").strip()
        source_id = source_id_from_url(url)
        kind = kind_from_source_id(source_id)
        if kind == "api" and not module:
            module = "未分组"
        if kind != "api" and not module:
            module = title
        entries.append(
            CatalogEntry(
                section=section,
                module=module,
                title=title,
                url=url,
                description=desc,
                kind=kind,
                source_id=source_id,
                source_file=source_file_from_url(url),
                module_slug=module_slug(module),
            )
        )
    return entries


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_yaml(path: Path, data: Any) -> None:
    text = yaml.dump(data, Dumper=NoAliasDumper, allow_unicode=True, sort_keys=False, width=120)
    write_text(path, text)


def write_json(path: Path, data: Any) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def clean_generated_dirs() -> None:
    for relative in [
        "assets",
        "docs/agent",
        "docs/external",
        "docs/guides",
        "docs/modules",
        "openapi/modules",
        "sources/external",
        "sources/pages",
    ]:
        target = ROOT / relative
        if not target.exists():
            continue
        target.relative_to(ROOT)
        shutil.rmtree(target)


def public_dict(entry: CatalogEntry) -> dict[str, str]:
    return dataclasses.asdict(entry)


def relative_link(current_file: Path, target_file: Path) -> str:
    return Path(os.path.relpath(target_file, start=current_file.parent)).as_posix()


def local_source_target(url: str, entries_by_source_id: dict[str, CatalogEntry]) -> Path | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc != "open.xiaoman.cn":
        return None
    match = LOCALIZABLE_SOURCE_RE.search(parsed.path)
    if not match:
        return None
    entry = entries_by_source_id.get(match.group(1))
    if entry is None:
        return None
    return ROOT / "sources" / "pages" / entry.source_file


def image_extension(url: str, content_type: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".jpeg", ".jpg", ".png", ".gif", ".webp", ".svg"}:
        return suffix
    return IMAGE_EXTENSIONS.get(content_type.lower(), ".bin")


def mirror_image(
    url: str,
    current_file: Path,
    image_cache: dict[str, Path],
    offline_report: dict[str, Any],
) -> str:
    if url not in image_cache:
        body, content_type = fetch_bytes(url)
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
        target = ROOT / "assets" / "images" / f"{digest}{image_extension(url, content_type)}"
        write_bytes(target, body)
        image_cache[url] = target
        offline_report["mirrored_images"].append(
            {
                "url": url,
                "local_path": str(target.relative_to(ROOT)),
                "content_type": content_type,
                "bytes": len(body),
            }
        )
    return relative_link(current_file, image_cache[url])


def yuque_slug(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    slug = path.rsplit("/", 1)[-1] if path else "index"
    slug = re.sub(r"[^0-9A-Za-z_-]+", "-", slug).strip("-")
    return slug or hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def metadata_text(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    return re.sub(r"https?://[^\s)\"'<>`]+", "EXTERNAL_URL", value)


def parse_html_metadata(html_text: str) -> dict[str, str]:
    allowed = {"description", "og:title", "og:description"}
    metadata: dict[str, str] = {}
    for tag in re.findall(r"<meta\s+[^>]*>", html_text, flags=re.IGNORECASE):
        attrs = {
            name.lower(): html_lib.unescape(value)
            for name, value in re.findall(r"([\w:-]+)=[\"']([^\"']*)[\"']", tag)
        }
        key = attrs.get("name") or attrs.get("property")
        if key in allowed and "content" in attrs:
            metadata[key] = metadata_text(attrs["content"])
    title = re.search(r"<title>(.*?)</title>", html_text, flags=re.IGNORECASE | re.DOTALL)
    if title:
        metadata["title"] = html_lib.unescape(re.sub(r"\s+", " ", title.group(1)).strip())
    return metadata


def parse_yuque_app_data(html_text: str) -> dict[str, Any]:
    match = re.search(r'window\.appData\s*=\s*JSON\.parse\(decodeURIComponent\("(.+?)"\)\);', html_text, re.DOTALL)
    if not match:
        return {}
    try:
        app_data = json.loads(urllib.parse.unquote(match.group(1)))
    except json.JSONDecodeError:
        return {}
    doc = app_data.get("doc") if isinstance(app_data, dict) else {}
    book = app_data.get("book") if isinstance(app_data, dict) else {}
    output: dict[str, Any] = {}
    if isinstance(doc, dict):
        output["doc"] = {
            key: doc.get(key)
            for key in [
                "id",
                "title",
                "slug",
                "description",
                "word_count",
                "created_at",
                "updated_at",
                "published_at",
                "content_updated_at",
            ]
            if doc.get(key) is not None
        }
        if "description" in output["doc"]:
            output["doc"]["description"] = metadata_text(output["doc"]["description"])
    if isinstance(book, dict):
        output["book"] = {key: book.get(key) for key in ["id", "name", "slug", "toc_updated_at"] if book.get(key) is not None}
        toc = book.get("toc")
        if isinstance(toc, list):
            output["api_toc"] = yuque_api_toc(toc)
    return output


def yuque_api_toc(toc: list[Any]) -> list[dict[str, Any]]:
    by_uuid = {item.get("uuid"): item for item in toc if isinstance(item, dict) and item.get("uuid")}
    api_roots = {uuid for uuid, item in by_uuid.items() if "API服务指引" in str(item.get("title", ""))}

    def under_api_root(item: dict[str, Any]) -> bool:
        uuid = item.get("uuid")
        while uuid and uuid in by_uuid:
            if uuid in api_roots:
                return True
            uuid = by_uuid[uuid].get("parent_uuid")
        return False

    rows: list[dict[str, Any]] = []
    for item in toc:
        if not isinstance(item, dict) or not under_api_root(item):
            continue
        rows.append(
            {
                "type": item.get("type", ""),
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "level": item.get("level", ""),
            }
        )
    return rows


def ensure_yuque_mirror(
    url: str,
    external_cache: dict[str, Path],
    offline_report: dict[str, Any],
) -> Path:
    if url not in external_cache:
        slug = yuque_slug(url)
        html_text = redact_text(fetch_text(url))
        html_path = ROOT / "sources" / "external" / "yuque" / f"{slug}.html"
        metadata = {
            "url": url,
            "html_snapshot": str(html_path.relative_to(ROOT)),
            "meta": parse_html_metadata(html_text),
            **parse_yuque_app_data(html_text),
        }
        metadata_path = ROOT / "sources" / "external" / "yuque" / f"{slug}.metadata.json"
        summary_path = ROOT / "docs" / "external" / "yuque" / f"{slug}.md"
        write_text(html_path, html_text)
        write_json(metadata_path, metadata)
        external_cache[url] = summary_path
        offline_report["mirrored_external_pages"].append(
            {
                "url": url,
                "local_html": str(html_path.relative_to(ROOT)),
                "local_metadata": str(metadata_path.relative_to(ROOT)),
                "local_summary": str(summary_path.relative_to(ROOT)),
            }
        )
    return external_cache[url]


def mirror_yuque_page(
    url: str,
    current_file: Path,
    external_cache: dict[str, Path],
    offline_report: dict[str, Any],
) -> str:
    return relative_link(current_file, ensure_yuque_mirror(url, external_cache, offline_report))


def mirror_yuque_api_toc_pages(external_cache: dict[str, Path], offline_report: dict[str, Any]) -> None:
    index = 0
    base_url = "https://www.yuque.com/help.xiaoman/irikgd/"
    while index < len(offline_report["mirrored_external_pages"]):
        item = offline_report["mirrored_external_pages"][index]
        index += 1
        metadata_path = ROOT / item["local_metadata"]
        with metadata_path.open(encoding="utf-8") as handle:
            metadata = json.load(handle)
        api_toc = metadata.get("api_toc")
        if not isinstance(api_toc, list):
            continue
        for toc_item in api_toc:
            if not isinstance(toc_item, dict) or toc_item.get("type") != "DOC":
                continue
            toc_url = str(toc_item.get("url") or "").strip()
            if not toc_url:
                continue
            url = toc_url if toc_url.startswith("https://") else urllib.parse.urljoin(base_url, toc_url)
            ensure_yuque_mirror(url, external_cache, offline_report)


def localize_markdown_links(
    markdown: str,
    current_file: Path,
    entries_by_source_id: dict[str, CatalogEntry],
    image_cache: dict[str, Path],
    external_cache: dict[str, Path],
    offline_report: dict[str, Any],
) -> str:
    def replace_link(match: re.Match[str]) -> str:
        marker, label, url, title = match.groups()
        title = title or ""
        if marker == "!":
            return f"![{label}]({mirror_image(url, current_file, image_cache, offline_report)}{title})"
        target = local_source_target(url, entries_by_source_id)
        if target is not None:
            return f"[{label}]({relative_link(current_file, target)}{title})"
        if urllib.parse.urlparse(url).netloc == "www.yuque.com":
            return f"[{label}]({mirror_yuque_page(url, current_file, external_cache, offline_report)}{title})"
        return match.group(0)

    def replace_plain_official_url(match: re.Match[str]) -> str:
        url = match.group(0)
        target = local_source_target(url, entries_by_source_id)
        return relative_link(current_file, target) if target is not None else url

    lines: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    fence_re = re.compile(r"^ {0,3}(`{3,}|~{3,})")
    for line in markdown.splitlines():
        fence = fence_re.match(line)
        if fence:
            marker = fence.group(1)
            if in_fence and marker.startswith(fence_char) and len(marker) >= fence_len:
                in_fence = False
                fence_char = ""
                fence_len = 0
            elif not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
            continue
        line = MARKDOWN_LINK_RE.sub(replace_link, line)
        line = re.sub(r"https://open\.xiaoman\.cn/[A-Za-z0-9_./-]*(?:api|doc|folder|schema)-\d+(?:\.md)?", replace_plain_official_url, line)
        lines.append(line)
    trailing_newline = "\n" if markdown.endswith("\n") else ""
    return "\n".join(lines) + trailing_newline


def fenced_blocks(markdown: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    lines = markdown.splitlines()
    i = 0
    start_re = re.compile(r"^ {0,3}(`{3,}|~{3,})([^`]*)$")
    while i < len(lines):
        match = start_re.match(lines[i])
        if not match:
            i += 1
            continue
        fence = match.group(1)
        fence_char = fence[0]
        fence_len = len(fence)
        lang = match.group(2).strip()
        i += 1
        content: list[str] = []
        close_re = re.compile(rf"^ {{0,3}}{re.escape(fence_char) + '{' + str(fence_len) + r',}'}\s*$")
        while i < len(lines) and not close_re.match(lines[i]):
            content.append(lines[i])
            i += 1
        if i < len(lines):
            i += 1
        blocks.append((lang, "\n".join(content).rstrip() + "\n"))
    return blocks


def extract_openapi(markdown: str) -> tuple[dict[str, Any] | None, str | None]:
    for lang, block in fenced_blocks(markdown):
        lang_name = (lang.split() or [""])[0].lower()
        if lang_name not in {"yaml", "yml"}:
            continue
        if "openapi:" not in block[:500]:
            continue
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError as exc:
            return None, f"yaml parse error: {exc}"
        if isinstance(parsed, dict) and "openapi" in parsed and "paths" in parsed:
            return parsed, None
    return None, "no openapi yaml block"


def first_operation(spec: dict[str, Any]) -> tuple[str, str, dict[str, Any]] | None:
    for path, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method.lower() in HTTP_METHODS and isinstance(operation, dict):
                return path, method.lower(), operation
    return None


def operation_id(method: str, path: str) -> str:
    normalized = path.strip("/") or "root"
    normalized = re.sub(r"\{([^}]+)\}", r"by_\1", normalized)
    normalized = re.sub(r"[^0-9A-Za-z]+", "_", normalized).strip("_").lower()
    return f"{method.lower()}_{normalized}"


def infer_module_from_path(path: str) -> str:
    first = path.strip("/").split("/", 2)
    segment = first[1] if len(first) > 1 and re.fullmatch(r"v\d+", first[0]) else first[0]
    if segment.lower() == "whatsapp":
        return "WhatsApp"
    return "未分组"


def module_from_operation(entry: CatalogEntry, path: str, operation: dict[str, Any]) -> str:
    if entry.module and entry.module != "未分组":
        return entry.module
    folder = operation.get("x-apifox-folder")
    if isinstance(folder, str) and folder.strip():
        return folder.strip()
    for tag in operation.get("tags", []) or []:
        if isinstance(tag, str) and not re.fullmatch(r"s\d+(?:\.\d+)*", tag):
            return tag
    return infer_module_from_path(path)


def normalize_operation(
    entry: CatalogEntry,
    method: str,
    path: str,
    operation: dict[str, Any],
    used_operation_ids: set[str],
) -> dict[str, Any]:
    op = deepcopy(operation)
    op.pop("x-run-in-apifox", None)
    module = module_from_operation(entry, path, op)
    tags = [tag for tag in op.get("tags", []) or [] if isinstance(tag, str)]
    if module not in tags:
        tags = [module, *tags]
    op["tags"] = tags
    base_id = operation_id(method, path)
    final_id = base_id
    suffix = 2
    while final_id in used_operation_ids:
        final_id = f"{base_id}_{suffix}"
        suffix += 1
    used_operation_ids.add(final_id)
    op["operationId"] = op.get("operationId") or final_id
    op["x-local-source-path"] = f"sources/pages/{entry.source_file}"
    op["x-source-id"] = entry.source_id
    op["x-source-title"] = entry.title
    op["x-source-module"] = module
    return op


def normalize_path_item(
    entry: CatalogEntry,
    path: str,
    path_item: dict[str, Any],
    used_operation_ids: set[str],
) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    for key, value in path_item.items():
        lower_key = key.lower()
        if lower_key in HTTP_METHODS and isinstance(value, dict):
            normalized[lower_key] = normalize_operation(entry, lower_key, path, value, used_operation_ids)
        else:
            normalized[key] = deepcopy(value)
    return normalized


def merge_components(target: dict[str, Any], source: dict[str, Any], source_id: str, report: dict[str, Any]) -> None:
    for group, values in (source or {}).items():
        if not isinstance(values, dict):
            target.setdefault(group, values)
            continue
        group_target = target.setdefault(group, {})
        if not isinstance(group_target, dict):
            report["component_conflicts"].append({"source": source_id, "group": group, "reason": "group type mismatch"})
            continue
        for name, value in values.items():
            if name not in group_target:
                group_target[name] = deepcopy(value)
            elif group_target[name] != value:
                report["component_conflicts"].append({"source": source_id, "group": group, "name": name})


def build_specs(entries: list[CatalogEntry], page_texts: dict[str, str], generated_at: str) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    full: dict[str, Any] = {
        "openapi": "3.0.1",
        "info": {
            "title": "Xiaoman OpenAPI (unofficial)",
            "version": generated_at[:10],
            "description": "Unofficial machine-readable OpenAPI bundle generated from public Xiaoman Open API documentation.",
        },
        "servers": [{"url": DEFAULT_SERVER, "description": "official documented server"}],
        "tags": [],
        "paths": {},
        "components": {
            "schemas": {},
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "description": "Token returned by POST /v1/oauth2/access_token. Official docs usually expose it as an Authorization header parameter.",
                }
            },
        },
        "x-generated-at": generated_at,
        "x-source": {"catalog": "sources/catalog.json", "snapshot": "sources/pages"},
    }
    report: dict[str, Any] = {"missing_openapi": [], "path_conflicts": [], "component_conflicts": []}
    operation_records: list[dict[str, Any]] = []
    used_operation_ids: set[str] = set()
    modules: dict[str, dict[str, Any]] = {}

    for entry in entries:
        if entry.kind != "api":
            continue
        markdown = page_texts.get(entry.source_file, "")
        spec, error = extract_openapi(markdown)
        if spec is None:
            report["missing_openapi"].append({**public_dict(entry), "error": error})
            continue
        merge_components(full["components"], spec.get("components", {}), entry.source_id, report)
        for path, path_item in (spec.get("paths") or {}).items():
            if not isinstance(path_item, dict):
                continue
            normalized_item = normalize_path_item(entry, path, path_item, used_operation_ids)
            for method, operation in normalized_item.items():
                if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                    continue
                target_path_item = full["paths"].setdefault(path, {})
                if method in target_path_item and target_path_item[method] != operation:
                    target_path_item[method].setdefault("x-xiaoman-duplicate-sources", []).append(
                        {"source_id": entry.source_id, "local_source": f"sources/pages/{entry.source_file}", "title": entry.title}
                    )
                    report["path_conflicts"].append(
                        {"path": path, "method": method.upper(), "kept": target_path_item[method].get("x-source-id"), "dropped": entry.source_id}
                    )
                    continue
                target_path_item[method] = operation
                module = operation.get("x-source-module") or entry.module or "未分组"
                module_spec = modules.setdefault(
                    module,
                    {
                        "openapi": "3.0.1",
                        "info": {
                            "title": f"Xiaoman OpenAPI - {module} (unofficial)",
                            "version": generated_at[:10],
                            "description": f"Unofficial module spec generated from public Xiaoman Open API documentation: {module}.",
                        },
                        "servers": [{"url": DEFAULT_SERVER, "description": "official documented server"}],
                        "tags": [{"name": module, "x-module-slug": module_slug(module)}],
                        "paths": {},
                        "components": deepcopy(full["components"]),
                        "x-generated-at": generated_at,
                        "x-source": {"catalog": "sources/catalog.json", "snapshot": "sources/pages"},
                    },
                )
                merge_components(module_spec["components"], spec.get("components", {}), entry.source_id, report)
                module_spec["paths"].setdefault(path, {})[method] = deepcopy(operation)
                operation_records.append(record_operation(entry, path, method, operation))

    modules = {module: spec for module, spec in sorted(modules.items(), key=lambda item: module_slug(item[0]))}
    operation_records.sort(key=lambda item: (module_slug(item["module"]), item["path"], item["method"]))
    module_names = sorted({record["module"] for record in operation_records}, key=module_slug)
    full["tags"] = [{"name": module, "x-module-slug": module_slug(module)} for module in module_names]
    return full, modules, operation_records, report


def schema_type(schema: Any) -> str:
    if not isinstance(schema, dict):
        return "unknown"
    parts = []
    if "$ref" in schema:
        parts.append(str(schema["$ref"]))
    if "type" in schema:
        parts.append(str(schema["type"]))
    if "format" in schema:
        parts.append(str(schema["format"]))
    if "enum" in schema:
        parts.append("enum")
    return "/".join(parts) if parts else "object"


def content_types(body: dict[str, Any] | None) -> list[str]:
    if not isinstance(body, dict):
        return []
    content = body.get("content")
    if not isinstance(content, dict):
        return []
    return list(content.keys())


def summarize_body(body: dict[str, Any] | None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not isinstance(body, dict):
        return rows
    for ctype, media in (body.get("content") or {}).items():
        schema = media.get("schema") if isinstance(media, dict) else {}
        row: dict[str, Any] = {"contentType": ctype, "schemaType": schema_type(schema)}
        if isinstance(schema, dict) and isinstance(schema.get("properties"), dict):
            required = set(schema.get("required") or [])
            row["fields"] = [
                {
                    "name": name,
                    "type": schema_type(prop),
                    "required": name in required,
                    "description": (prop or {}).get("description", "") if isinstance(prop, dict) else "",
                }
                for name, prop in schema["properties"].items()
            ]
        rows.append(row)
    return rows


def record_operation(entry: CatalogEntry, path: str, method: str, operation: dict[str, Any]) -> dict[str, Any]:
    module = operation.get("x-source-module") or entry.module
    parameters = []
    for parameter in operation.get("parameters") or []:
        if not isinstance(parameter, dict):
            continue
        schema = parameter.get("schema") if isinstance(parameter.get("schema"), dict) else {}
        parameters.append(
            {
                "name": parameter.get("name", ""),
                "in": parameter.get("in", ""),
                "required": bool(parameter.get("required")),
                "type": schema_type(schema),
                "description": parameter.get("description", ""),
                "example": parameter.get("example", schema.get("example") if isinstance(schema, dict) else None),
            }
        )
    responses = []
    for status, response in (operation.get("responses") or {}).items():
        if not isinstance(response, dict):
            responses.append({"status": str(status)})
            continue
        responses.append(
            {
                "status": str(status),
                "description": response.get("description", ""),
                "contentTypes": list((response.get("content") or {}).keys()) if isinstance(response.get("content"), dict) else [],
            }
        )
    return {
        "id": operation.get("operationId"),
        "module": module,
        "moduleSlug": module_slug(module),
        "title": entry.title,
        "summary": operation.get("summary", entry.title),
        "method": method.upper(),
        "path": path,
        "tags": operation.get("tags", []),
        "source": f"sources/pages/{entry.source_file}",
        "localSource": f"sources/pages/{entry.source_file}",
        "sourceId": entry.source_id,
        "description": operation.get("description", ""),
        "parameters": parameters,
        "requestBody": summarize_body(operation.get("requestBody")),
        "requestContentTypes": content_types(operation.get("requestBody")),
        "responses": responses,
    }


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    output = []
    for idx, row in enumerate(rows):
        output.append("| " + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |")
        if idx == 0:
            output.append("| " + " | ".join("-" * widths[i] for i in range(len(row))) + " |")
    return "\n".join(output)


def one_line(value: Any, limit: int = 160) -> str:
    text = str(value or "").replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text[: limit - 1] + "…" if len(text) > limit else text


def render_module_markdown(module: str, records: list[dict[str, Any]], generated_at: str) -> str:
    lines = [
        f"# {module}",
        "",
        f"- generated_at: `{generated_at}`",
        f"- openapi: `../../openapi/modules/{module_slug(module)}.openapi.yaml`",
        f"- endpoints: `{len(records)}`",
        "",
    ]
    for record in records:
        lines.extend(
            [
                f"## {record['method']} {record['path']}",
                "",
                f"- operationId: `{record['id']}`",
                f"- summary: {record['summary']}",
                f"- source: `../../{record['localSource']}`",
            ]
        )
        params = record.get("parameters") or []
        if params:
            rows = [["in", "name", "type", "required", "description"]]
            for param in params:
                rows.append(
                    [
                        param.get("in", ""),
                        param.get("name", ""),
                        param.get("type", ""),
                        "yes" if param.get("required") else "no",
                        one_line(param.get("description", "")),
                    ]
                )
            lines.extend(["", "### parameters", "", markdown_table(rows)])
        bodies = record.get("requestBody") or []
        if bodies:
            lines.extend(["", "### requestBody"])
            for body in bodies:
                lines.append(f"- contentType: `{body.get('contentType')}` schema: `{body.get('schemaType')}`")
                fields = body.get("fields") or []
                if fields:
                    rows = [["name", "type", "required", "description"]]
                    for field in fields[:80]:
                        rows.append(
                            [
                                field.get("name", ""),
                                field.get("type", ""),
                                "yes" if field.get("required") else "no",
                                one_line(field.get("description", "")),
                            ]
                        )
                    lines.extend(["", markdown_table(rows)])
                    if len(fields) > 80:
                        lines.append(f"\n_omitted {len(fields) - 80} additional top-level fields; see OpenAPI file._")
        responses = record.get("responses") or []
        if responses:
            rows = [["status", "contentTypes", "description"]]
            for response in responses:
                rows.append(
                    [
                        response.get("status", ""),
                        ", ".join(response.get("contentTypes") or []),
                        one_line(response.get("description", "")),
                    ]
                )
            lines.extend(["", "### responses", "", markdown_table(rows)])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_api_index(records: list[dict[str, Any]], generated_at: str) -> str:
    rows = [["module", "method", "path", "summary", "operationId"]]
    for record in records:
        rows.append([record["module"], record["method"], record["path"], record["summary"], record["id"]])
    return "\n".join(
        [
            "# Xiaoman OpenAPI Endpoint Index",
            "",
            f"generated_at: `{generated_at}`",
            "",
            markdown_table(rows),
            "",
        ]
    )


def render_source_index(entries: list[CatalogEntry], generated_at: str) -> str:
    rows = [["kind", "module", "title", "source_id", "local_source"]]
    for entry in sorted(entries, key=lambda item: (item.kind, item.module_slug, item.source_id)):
        rows.append([entry.kind, entry.module, entry.title, entry.source_id, f"`sources/pages/{entry.source_file}`"])
    return "\n".join(
        [
            "# Xiaoman OpenAPI Source Index",
            "",
            f"generated_at: `{generated_at}`",
            "",
            "Every public Xiaoman Markdown page listed by the official `llms.txt` catalog is copied under `sources/pages/`. This index intentionally points to local files; official URLs are retained in `sources/catalog.json` and reports for attribution and upstream comparison.",
            "",
            markdown_table(rows),
            "",
        ]
    )


def render_guides_index(entries: list[CatalogEntry], generated_at: str) -> str:
    rows = [["kind", "module", "title", "guide", "source_snapshot"]]
    for entry in sorted((item for item in entries if item.kind != "api"), key=lambda item: (item.kind, item.module_slug, item.source_id)):
        rows.append(
            [
                entry.kind,
                entry.module,
                entry.title,
                f"`docs/guides/{entry.source_id}.md`",
                f"`sources/pages/{entry.source_file}`",
            ]
        )
    return "\n".join(
        [
            "# Xiaoman OpenAPI Guide Index",
            "",
            f"generated_at: `{generated_at}`",
            "",
            "Local non-endpoint guide pages mirrored from the public Xiaoman catalog. These pages provide onboarding, module notes, and schema-level context for the API contract.",
            "",
            markdown_table(rows),
            "",
        ]
    )


def render_yuque_summary(metadata: dict[str, Any], generated_at: str) -> str:
    doc = metadata.get("doc") if isinstance(metadata.get("doc"), dict) else {}
    meta = metadata.get("meta") if isinstance(metadata.get("meta"), dict) else {}
    title = doc.get("title") or meta.get("og:title") or meta.get("title") or yuque_slug(str(metadata.get("url", "")))
    description = doc.get("description") or meta.get("description") or meta.get("og:description") or ""
    lines = [
        f"# {title}",
        "",
        f"- generated_at: `{generated_at}`",
        f"- html_snapshot: `../../../{metadata['html_snapshot']}`",
        f"- metadata: `../../../{metadata['local_metadata']}`",
    ]
    for key in ["word_count", "published_at", "content_updated_at", "updated_at"]:
        if doc.get(key) is not None:
            lines.append(f"- {key}: `{doc[key]}`")
    if description:
        lines.extend(["", "## Description", "", one_line(description, 1000)])
    api_toc = metadata.get("api_toc")
    if isinstance(api_toc, list) and api_toc:
        rows = [["level", "type", "title", "local_summary"]]
        for item in api_toc:
            toc_url = str(item.get("url", "") or "")
            local_summary = ""
            if item.get("type") == "DOC" and toc_url:
                local_summary = f"{yuque_slug(toc_url)}.md"
            rows.append([str(item.get("level", "")), str(item.get("type", "")), str(item.get("title", "")), local_summary])
        lines.extend(["", "## API Service TOC", "", markdown_table(rows)])
    return "\n".join(lines).rstrip() + "\n"


def write_yuque_summaries(offline_report: dict[str, Any], generated_at: str) -> None:
    rows = [["title", "summary", "html_snapshot", "metadata"]]
    for item in offline_report["mirrored_external_pages"]:
        metadata_path = ROOT / item["local_metadata"]
        with metadata_path.open(encoding="utf-8") as handle:
            metadata = json.load(handle)
        metadata["local_metadata"] = item["local_metadata"]
        summary_path = ROOT / item["local_summary"]
        write_text(summary_path, render_yuque_summary(metadata, generated_at))
        doc = metadata.get("doc") if isinstance(metadata.get("doc"), dict) else {}
        meta = metadata.get("meta") if isinstance(metadata.get("meta"), dict) else {}
        title = doc.get("title") or meta.get("og:title") or meta.get("title") or yuque_slug(str(metadata.get("url", "")))
        rows.append(
            [
                str(title),
                f"`{item['local_summary']}`",
                f"`{item['local_html']}`",
                f"`{item['local_metadata']}`",
            ]
        )
    if len(rows) == 1:
        return
    write_text(
        ROOT / "docs" / "external" / "yuque.md",
        "\n".join(
            [
                "# Linked Yuque Guide Snapshots",
                "",
                f"generated_at: `{generated_at}`",
                "",
                "Xiaoman guide pages link to these Yuque pages. The public HTML snapshots and extracted metadata are mirrored locally; the per-page Markdown summaries are the AI-facing entry points.",
                "",
                markdown_table(rows),
                "",
            ]
        ),
    )


def render_readme(entries: list[CatalogEntry], records: list[dict[str, Any]], generated_at: str) -> str:
    modules = sorted({record["module"] for record in records}, key=module_slug)
    module_lines = [f"- [{module}](docs/modules/{module_slug(module)}.md): `{module_slug(module)}`" for module in modules]
    return "\n".join(
        [
            "# xiaoman-openapi",
            "",
            "Unofficial AI-readable OpenAPI and Markdown bundle for Xiaoman Open API.",
            "",
            "## Invariant",
            "",
            "The public Xiaoman `.md` pages are the input source. Generated OpenAPI files and agent Markdown are derived artifacts. Do not edit generated files by hand; update the sync script and regenerate.",
            "",
            "## Files",
            "",
            "- `openapi/xiaoman.openapi.yaml`: full merged OpenAPI 3.0.1 document.",
            "- `openapi/modules/*.openapi.yaml`: module-level OpenAPI documents.",
            "- `docs/modules/*.md`: compact agent-facing Markdown generated from OpenAPI operations.",
            "- `docs/api-index.md`: endpoint table for quick retrieval.",
            "- `docs/guides-index.md`: local index of non-endpoint Xiaoman guide pages.",
            "- `docs/source-index.md`: local source snapshot index.",
            "- `docs/external/yuque/*.md`: AI-facing summaries for linked Yuque guide snapshots.",
            "- `docs/agent/endpoints.jsonl`: one endpoint per line for embedding/indexing pipelines.",
            "- `sources/pages/*.md`: fetched public Xiaoman Markdown pages.",
            "- `sources/external/`: mirrored external guide snapshots linked from Xiaoman pages.",
            "- `assets/images/`: mirrored Markdown images used by the guide pages.",
            "- `reports/sync-report.json`: extraction warnings and conflict report.",
            "- `reports/external-links.json`: classified external URLs found in generated text files.",
            "",
            "## How AI Agents Should Use This",
            "",
            "Start from the smallest stable context, then load the exact contract only when needed.",
            "",
            "1. Read `llms.txt` as the repository entry point.",
            "2. Locate the endpoint in `docs/api-index.md` or `docs/agent/endpoints.jsonl`.",
            "3. Read the matching `docs/modules/<module>.md` for compact human-readable context.",
            "4. Use `openapi/modules/<module>.openapi.yaml` as the request/response contract.",
            "5. Use `sources/pages/*.md` only when you need to inspect the mirrored Xiaoman page content.",
            "6. Use `docs/guides-index.md` and `docs/external/yuque.md` for onboarding and linked guide context.",
            "",
            "Do not load `openapi/xiaoman.openapi.yaml` into an LLM context by default. The full file is for OpenAPI tools, code generators, validators, and offline indexing. Agent workflows should prefer module specs.",
            "",
            "### Remote Agent Prompt",
            "",
            "```text",
            "You are integrating with Xiaoman Open API.",
            "First read:",
            "https://raw.githubusercontent.com/frankie0736/xiaoman-openapi/main/llms.txt",
            "",
            "Find endpoints via docs/api-index.md or docs/agent/endpoints.jsonl.",
            "For implementation, use the matching openapi/modules/*.openapi.yaml file as the source of truth.",
            "Do not infer request fields from the web UI. If Markdown and OpenAPI conflict, trust OpenAPI.",
            "```",
            "",
            "### Use Inside Another Repository",
            "",
            "```bash",
            "git submodule add https://github.com/frankie0736/xiaoman-openapi docs/vendor/xiaoman-openapi",
            "```",
            "",
            "Then point your coding agent at:",
            "",
            "```text",
            "docs/vendor/xiaoman-openapi/llms.txt",
            "docs/vendor/xiaoman-openapi/docs/api-index.md",
            "docs/vendor/xiaoman-openapi/openapi/modules/*.openapi.yaml",
            "```",
            "",
            "### RAG / Tooling Input",
            "",
            "Use `docs/agent/endpoints.jsonl` for retrieval. Each line is one endpoint with module, method, path, parameters, request body summary, responses, and local source path. After retrieval, load the module OpenAPI file before generating code.",
            "",
            "## Offline Coverage",
            "",
            "The API guide is offline-complete for the official public pages listed in Xiaoman's `llms.txt` at sync time. Those pages are copied to `sources/pages/`, generated guides point to local files, and each generated endpoint includes `source` / `localSource` / `x-local-source-path` pointing back to the local snapshot.",
            "",
            "Markdown images used by guide pages are mirrored under `assets/images/`. Yuque guide links referenced by Xiaoman pages are mirrored under `sources/external/yuque/` with AI-facing summaries in `docs/external/yuque/`.",
            "",
            "Remaining external URLs are classified in `reports/external-links.json`. They should be runtime API servers, example payload values, repository usage links, attribution metadata, or assets embedded inside archived external HTML snapshots. They are not required to read the API guide offline.",
            "",
            "## Modules",
            "",
            *module_lines,
            "",
            "## Regenerate",
            "",
            "```bash",
            "python3 -m pip install -r requirements.txt",
            "python3 tools/sync_xiaoman_docs.py",
            "python3 tools/validate_openapi.py",
            "python3 tools/check_offline_docs.py",
            "python3 tools/check_no_secrets.py",
            "```",
            "",
            "## Source",
            "",
            f"- catalog: `{LLMS_URL}`",
            "- official site: `https://open.xiaoman.cn`",
            f"- last generated: `{generated_at}`",
            f"- fetched pages: `{len(entries)}`",
            f"- extracted endpoints: `{len(records)}`",
            "",
            "## Notice",
            "",
            "This repository is not affiliated with Xiaoman. API descriptions are generated from publicly available Xiaoman documentation. Xiaoman owns its product names and official documentation content. See `NOTICE.md`.",
            "",
            "## License",
            "",
            "Repository tooling is MIT licensed. Generated documentation is derived from Xiaoman public documentation and may be subject to Xiaoman's original terms.",
            "",
        ]
    )


def render_llms(modules: list[str], records: list[dict[str, Any]]) -> str:
    lines = [
        "# xiaoman-openapi",
        "",
        "> Unofficial AI-readable OpenAPI and Markdown bundle for Xiaoman Open API.",
        "",
        "## OpenAPI",
        "- [Full OpenAPI YAML](openapi/xiaoman.openapi.yaml)",
        "- [Full OpenAPI JSON](openapi/xiaoman.openapi.json)",
        "",
        "## Agent Index",
        "- [Endpoint index](docs/api-index.md)",
        "- [Endpoint JSONL](docs/agent/endpoints.jsonl)",
        "- [Guide index](docs/guides-index.md)",
        "- [Source snapshot index](docs/source-index.md)",
        "- [Linked Yuque guide snapshots](docs/external/yuque.md)",
        "",
        "## Modules",
    ]
    for module in modules:
        slug = module_slug(module)
        count = sum(1 for record in records if record["module"] == module)
        lines.append(f"- [{module}](docs/modules/{slug}.md): {count} endpoints; OpenAPI `openapi/modules/{slug}.openapi.yaml`")
    lines.append("")
    return "\n".join(lines)


def render_llms_full(modules: list[str], records_by_module: dict[str, list[dict[str, Any]]], generated_at: str) -> str:
    lines = [
        "# xiaoman-openapi full agent context",
        "",
        f"generated_at: `{generated_at}`",
        "",
        "Use `openapi/xiaoman.openapi.yaml` as the API contract. The Markdown below is a retrieval-friendly summary.",
        "",
    ]
    for module in modules:
        lines.append(render_module_markdown(module, records_by_module[module], generated_at))
    return "\n".join(lines).rstrip() + "\n"


def classify_external_url(relative_file: str, url: str) -> str:
    host = urllib.parse.urlparse(url).netloc
    if relative_file.startswith("sources/external/yuque/") and relative_file.endswith(".html"):
        return "archived-html-asset"
    if host == "api-sandbox.xiaoman.cn":
        return "runtime-server"
    if host == "test.xiaoman.cn":
        return "example-callback"
    if host in {"example.com", "www.example.com"}:
        return "example-data"
    if host.endswith("oss-cn-hangzhou.aliyuncs.com") or host.endswith(".aliyuncs.com"):
        return "example-data"
    if host == "open.xiaoman.cn":
        return "official-upstream-metadata"
    if host == "www.yuque.com":
        return "mirrored-external-guide-metadata"
    if host in {"github.com", "raw.githubusercontent.com"}:
        return "repository-usage"
    return "unclassified-external"


def iter_report_text_files() -> list[Path]:
    paths: list[Path] = [ROOT / "README.md", ROOT / "llms.txt", ROOT / "llms-full.txt"]
    for relative in ["docs", "openapi", "sources"]:
        root = ROOT / relative
        if not root.exists():
            continue
        paths.extend(path for path in root.rglob("*") if path.is_file())
    return sorted(paths)


def external_link_report() -> dict[str, Any]:
    url_re = re.compile(r"""https?://[^\s)\]"'<>`]+""")
    by_category: dict[str, dict[str, Any]] = {}
    by_host: dict[str, dict[str, Any]] = {}
    for path in iter_report_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative_file = str(path.relative_to(ROOT))
        for line_no, line in enumerate(text.splitlines(), start=1):
            for url in url_re.findall(line):
                host = urllib.parse.urlparse(url).netloc
                category = classify_external_url(relative_file, url)
                host_item = by_host.setdefault(host, {"count": 0, "categories": {}, "examples": []})
                host_item["count"] += 1
                host_item["categories"][category] = host_item["categories"].get(category, 0) + 1
                if len(host_item["examples"]) < 20:
                    host_item["examples"].append({"file": relative_file, "line": line_no, "url": url, "category": category})
                category_item = by_category.setdefault(category, {"count": 0, "examples": []})
                category_item["count"] += 1
                if len(category_item["examples"]) < 20:
                    category_item["examples"].append({"file": relative_file, "line": line_no, "url": url})
    return {
        "categories": dict(sorted(by_category.items(), key=lambda pair: (-pair[1]["count"], pair[0]))),
        "hosts": dict(sorted(by_host.items(), key=lambda pair: (-pair[1]["count"], pair[0]))),
    }


def write_guides(
    entries: list[CatalogEntry],
    page_texts: dict[str, str],
    generated_at: str,
    entries_by_source_id: dict[str, CatalogEntry],
    image_cache: dict[str, Path],
    external_cache: dict[str, Path],
    offline_report: dict[str, Any],
) -> None:
    for entry in entries:
        if entry.kind == "api":
            continue
        slug = source_id_from_url(entry.url)
        current_file = ROOT / "docs" / "guides" / f"{slug}.md"
        frontmatter = {
            "title": entry.title,
            "module": entry.module,
            "source_id": entry.source_id,
            "local_source": f"../../sources/pages/{entry.source_file}",
            "generated_at": generated_at,
        }
        text = "---\n" + yaml.dump(frontmatter, Dumper=NoAliasDumper, allow_unicode=True, sort_keys=False).strip() + "\n---\n\n"
        body = localize_markdown_links(
            page_texts.get(entry.source_file, "").strip(),
            current_file,
            entries_by_source_id,
            image_cache,
            external_cache,
            offline_report,
        )
        text += body.strip() + "\n"
        write_text(current_file, text)


def sync() -> None:
    generated_at = now_iso()
    clean_generated_dirs()
    llms_text = fetch_text(LLMS_URL)
    entries = parse_catalog(llms_text)
    if not entries:
        raise RuntimeError("no catalog entries parsed from llms.txt")
    entries_by_source_id = {entry.source_id: entry for entry in entries}
    image_cache: dict[str, Path] = {}
    external_cache: dict[str, Path] = {}
    offline_report: dict[str, Any] = {"mirrored_images": [], "mirrored_external_pages": []}

    write_text(ROOT / "sources" / "llms.txt", llms_text)
    write_json(ROOT / "sources" / "catalog.json", [public_dict(entry) for entry in entries])

    page_texts: dict[str, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(fetch_text, entry.url): entry for entry in entries}
        for future in concurrent.futures.as_completed(future_map):
            entry = future_map[future]
            try:
                text = redact_text(future.result())
            except Exception as exc:
                raise RuntimeError(f"failed to fetch {entry.url}") from exc
            page_texts[entry.source_file] = text

    for entry in entries:
        current_file = ROOT / "sources" / "pages" / entry.source_file
        write_text(
            current_file,
            localize_markdown_links(
                page_texts[entry.source_file],
                current_file,
                entries_by_source_id,
                image_cache,
                external_cache,
                offline_report,
            ),
        )
    mirror_yuque_api_toc_pages(external_cache, offline_report)

    full, modules, operation_records, report = build_specs(entries, page_texts, generated_at)
    report["generated_at"] = generated_at
    report["catalog_entries"] = len(entries)
    report["api_pages"] = sum(1 for entry in entries if entry.kind == "api")
    report["extracted_operations"] = len(operation_records)
    report["offline"] = offline_report

    write_yaml(ROOT / "openapi" / "xiaoman.openapi.yaml", full)
    write_json(ROOT / "openapi" / "xiaoman.openapi.json", full)
    for module, spec in modules.items():
        slug = module_slug(module)
        write_yaml(ROOT / "openapi" / "modules" / f"{slug}.openapi.yaml", spec)
        write_json(ROOT / "openapi" / "modules" / f"{slug}.openapi.json", spec)

    records_by_module: dict[str, list[dict[str, Any]]] = {}
    for record in operation_records:
        records_by_module.setdefault(record["module"], []).append(record)
    modules_order = sorted(records_by_module, key=module_slug)
    for module in modules_order:
        write_text(ROOT / "docs" / "modules" / f"{module_slug(module)}.md", render_module_markdown(module, records_by_module[module], generated_at))

    write_text(ROOT / "docs" / "api-index.md", render_api_index(operation_records, generated_at))
    write_text(ROOT / "docs" / "source-index.md", render_source_index(entries, generated_at))
    write_text(ROOT / "docs" / "guides-index.md", render_guides_index(entries, generated_at))
    write_text(
        ROOT / "docs" / "agent" / "endpoints.jsonl",
        "\n".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) for record in operation_records) + "\n",
    )
    write_guides(entries, page_texts, generated_at, entries_by_source_id, image_cache, external_cache, offline_report)
    write_yuque_summaries(offline_report, generated_at)
    write_text(ROOT / "README.md", render_readme(entries, operation_records, generated_at))
    write_text(ROOT / "llms.txt", render_llms(modules_order, operation_records))
    write_text(ROOT / "llms-full.txt", render_llms_full(modules_order, records_by_module, generated_at))
    write_json(ROOT / "reports" / "sync-report.json", report)
    write_json(ROOT / "reports" / "external-links.json", external_link_report())
    print(
        json.dumps(
            {
                "catalog_entries": len(entries),
                "api_pages": report["api_pages"],
                "extracted_operations": len(operation_records),
                "missing_openapi": len(report["missing_openapi"]),
                "path_conflicts": len(report["path_conflicts"]),
                "component_conflicts": len(report["component_conflicts"]),
            },
            ensure_ascii=False,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync public Xiaoman API docs into OpenAPI and agent Markdown.")
    parser.parse_args()
    sync()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
