#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
HTTP_METHODS = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: root must be an object")
    return data


def validate_spec(path: Path) -> dict[str, int]:
    spec = load_yaml(path)
    errors: list[str] = []
    if not str(spec.get("openapi", "")).startswith("3."):
        errors.append("openapi must be 3.x")
    if not isinstance(spec.get("info"), dict):
        errors.append("info must exist")
    if not isinstance(spec.get("paths"), dict):
        errors.append("paths must exist")
    operation_count = 0
    operation_ids: set[str] = set()
    for api_path, path_item in (spec.get("paths") or {}).items():
        if not isinstance(path_item, dict):
            errors.append(f"{api_path}: path item must be object")
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            operation_count += 1
            if not isinstance(operation, dict):
                errors.append(f"{method.upper()} {api_path}: operation must be object")
                continue
            if not operation.get("operationId"):
                errors.append(f"{method.upper()} {api_path}: missing operationId")
            elif operation["operationId"] in operation_ids:
                errors.append(f"{method.upper()} {api_path}: duplicate operationId {operation['operationId']}")
            else:
                operation_ids.add(operation["operationId"])
            if not isinstance(operation.get("responses"), dict) or not operation["responses"]:
                errors.append(f"{method.upper()} {api_path}: missing responses")
    if errors:
        raise ValueError(f"{path} failed validation:\n" + "\n".join(f"- {error}" for error in errors))
    return {"operations": operation_count}


def main() -> int:
    paths = [ROOT / "openapi" / "xiaoman.openapi.yaml"]
    paths.extend(sorted((ROOT / "openapi" / "modules").glob("*.openapi.yaml")))
    total = 0
    results = {}
    for path in paths:
        result = validate_spec(path)
        total += result["operations"]
        results[str(path.relative_to(ROOT))] = result
    print(json.dumps({"files": len(paths), "operation_entries": total, "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
