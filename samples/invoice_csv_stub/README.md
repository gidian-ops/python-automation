# Invoice → CSV stub

Parses a plain `key: value` invoice text file into a CSV row. Useful as a starting point for PDF/OCR pipelines without baking in paid APIs.

```bash
python to_csv.py --input sample_invoice.txt --out /tmp/invoice.csv
```
