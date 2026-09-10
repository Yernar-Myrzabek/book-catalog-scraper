# Book Catalog Scraper

A Python web scraper that collects product data from every page of an online catalog and exports it to a clean CSV file, ready to open in Excel or Google Sheets.

## What it does

- Automatically crawls all pages of a paginated product catalog
- Extracts: **title, price, stock availability**
- Fixes common encoding issues (e.g. broken currency symbols)
- Saves everything into a single structured CSV file
- Includes a polite delay between requests to avoid overloading the server

## Result

Collected **1,000 products** across **50 pages** in under a minute.

## Tech stack

- Python
- `requests` — fetching page content
- `BeautifulSoup` — parsing HTML and extracting data
- `csv` — exporting structured results

## Example output (books.csv)

| title                  | price  | availability |
|------------------------|--------|--------------|
| A Light in the Attic   | £51.77 | In stock     |
| Tipping the Velvet     | £53.74 | In stock     |
| Soumission             | £50.10 | In stock     |

## How to run

```bash
pip install requests beautifulsoup4
python scraper.py
```

The script will generate `books.csv` in the same folder.

## Use cases

This same approach can be adapted for:
- Competitor price monitoring
- Marketplace product exports (Amazon, eBay, Wildberries, etc.)
- Lead generation from directory-style websites
- Any catalog-style site with predictable page URLs

---

