#!/usr/bin/env python3
"""Fetch a list of URLs into local HTML files with basic retries."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.parse import urlparse

import requests


def load_urls(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def safe_name(url: str, index: int) -> str:
    host = urlparse(url).netloc.replace(":", "_") or "page"
    return f"{index:03d}_{host}.html"


def fetch_one(session: requests.Session, url: str, dest: Path, retries: int = 3) -> dict:
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            return {
                "url": url,
                "path": str(dest),
                "status": resp.status_code,
                "bytes": len(resp.content),
                "ok": True,
            }
        except requests.RequestException as exc:
            last_error = str(exc)
            time.sleep(attempt)
    return {"url": url, "path": str(dest), "ok": False, "error": last_error}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--urls", type=Path, required=True, help="Text file with one URL per line")
    parser.add_argument("--out", type=Path, required=True, help="Output directory for HTML files")
    args = parser.parse_args()

    urls = load_urls(args.urls)
    args.out.mkdir(parents=True, exist_ok=True)
    manifest = []
    with requests.Session() as session:
        session.headers.update({"User-Agent": "gidian-ops-sample-fetcher/1.0"})
        for i, url in enumerate(urls, start=1):
            dest = args.out / safe_name(url, i)
            result = fetch_one(session, url, dest)
            manifest.append(result)
            status = "ok" if result["ok"] else "fail"
            print(f"[{status}] {url}")

    manifest_path = args.out / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {manifest_path}")


if __name__ == "__main__":
    main()
