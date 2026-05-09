#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_DOC_RE = re.compile(r"https://open\.xiaoman\.cn/(?:apidoc/[^)\s]+|(?:api|doc|folder|schema)-\d+(?:\.md)?)")
REMOTE_MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*]\(https?://")
REMOTE_YUQUE_RE = re.compile(r"https://www\.yuque\.com/help\.xiaoman/")


def markdown_files() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "llms.txt", ROOT / "llms-full.txt"]
    for relative in ["docs", "sources/pages"]:
        root = ROOT / relative
        if root.exists():
            paths.extend(sorted(root.rglob("*.md")))
    return [path for path in paths if path.exists()]


def non_code_lines(path: Path):
    in_fence = False
    fence_char = ""
    fence_len = 0
    fence_re = re.compile(r"^ {0,3}(`{3,}|~{3,})")
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
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
            continue
        if not in_fence:
            yield line_no, line


def main() -> int:
    findings: list[str] = []
    for path in markdown_files():
        relative = path.relative_to(ROOT)
        for line_no, line in non_code_lines(path):
            if OFFICIAL_DOC_RE.search(line):
                findings.append(f"{relative}:{line_no}: official Xiaoman doc link should point to local snapshot")
            if REMOTE_MARKDOWN_IMAGE_RE.search(line):
                findings.append(f"{relative}:{line_no}: remote Markdown image should be mirrored under assets/images")
            if REMOTE_YUQUE_RE.search(line):
                findings.append(f"{relative}:{line_no}: Yuque guide link should point to local snapshot summary")
    if findings:
        print("offline documentation violations found:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("offline documentation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
