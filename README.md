# Python automation samples

Public samples from **Gidian** (South Africa) for scoped automation and agent-style workflows.

These are small, runnable examples meant for clients who want a clear deliverable: scripts, a README, and a hand-off checklist. Not a claim of past client logos or live trading results.

## Samples

| Folder | What it does |
| --- | --- |
| `samples/html_batch_fetcher` | Download a list of URLs to local HTML files with retries and a simple manifest |
| `samples/invoice_csv_stub` | Parse structured fields from a sample invoice text file into CSV (no paid APIs) |

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python samples/html_batch_fetcher/fetch.py --urls samples/html_batch_fetcher/urls.txt --out /tmp/pages
python samples/invoice_csv_stub/to_csv.py --input samples/invoice_csv_stub/sample_invoice.txt --out /tmp/invoice.csv
```

## Positioning

I deliver fixed-scope automation packs (Python scripts, multi-agent / ops prompts, docs) for builders and small teams. Typical package: working scripts + README + hand-off notes.

Contact: Upwork profile for **Gidian**.
