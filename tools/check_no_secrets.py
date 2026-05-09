#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".venv"}
PATTERNS = [
    ("github_token", re.compile(r"gh[opsu]_[A-Za-z0-9_]{20,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("whatsapp_token", re.compile(r"biai-whatsapp-(?!REDACTED)[A-Za-z0-9_-]{16,}")),
    ("client_secret_value", re.compile(r"(?i)client_secret\s*[:=]\s*[\"'][A-Za-z0-9_-]{16,}")),
    ("webhook_secret_key", re.compile(r"(?i)secretKey\s*=\s*[\"'](?!REDACTED)[A-Za-z0-9+/=]{24,}[\"']")),
    ("webhook_signature", re.compile(r"(?i)signature\s*=\s*[\"'](?!REDACTED)[a-f0-9]{32,}[\"']")),
]


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def main() -> int:
    findings = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for name, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{line_no}: {name}")
    if findings:
        print("secret-like values found:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("no secret-like values found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
