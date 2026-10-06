#!/usr/bin/env python3
"""Turn a simple key: value invoice text file into a one-row CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


KEYS = ("invoice_id", "vendor", "date", "total", "currency")


def parse_invoice(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip().lower()] = value.strip()
    return {k: data.get(k, "") for k in KEYS}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    row = parse_invoice(args.input.read_text(encoding="utf-8"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=KEYS)
        writer.writeheader()
        writer.writerow(row)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
