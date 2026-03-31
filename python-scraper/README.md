# Python Web Scraper

A Python web scraper built with [Requests](https://docs.python-requests.org/) and
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) that mirrors the
companion [Go scraper](../scraper/README.md) while adding extra capabilities.

## Features

| Feature | Go scraper | Python scraper |
|---|:---:|:---:|
| Page title | yes | yes |
| Extract links | yes | yes |
| Extract headers (h1/h2/h3) | yes | yes |
| JSON output | yes | yes |
| meta description & keywords | no | yes |
| Image URL extraction | no | yes |
| HTTP status code | no | yes |
| Save to JSON file | no | yes |
| Save to CSV file | no | yes |
| Importable as a Python library | no | yes |

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage

```bash
python scraper.py --url https://example.com
```

### JSON output to stdout

```bash
python scraper.py --url https://example.com --json
```

### Save results to files

```bash
python scraper.py --url https://example.com --output results.json --csv results.csv
```

### All flags

```
--url URL            URL to scrape (required)
--json               Print results as JSON to stdout
--output FILE        Save results as JSON to FILE
--csv FILE           Save results as CSV to FILE
--timeout SECONDS    HTTP request timeout (default: 10)
--user-agent STRING  Custom User-Agent header
```

## Example Output

### Plain text

```
=== Scrape Results ===
URL:    https://example.com
Status: 200
Title:  Example Domain

--- Headers ---
  - Example Domain

--- Links ---
  - https://www.iana.org/domains/example

--- Images ---
```

### JSON

```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "links": ["https://www.iana.org/domains/example"],
  "headers": ["Example Domain"],
  "meta_description": "",
  "meta_keywords": "",
  "images": [],
  "status_code": 200
}
```

## Using as a Library

```python
from scraper import scrape, print_results, save_json, save_csv

data = scrape("https://example.com")
print(data.title)
print(data.status_code)
print(data.links)

print_results(data)
save_json(data, "results.json")
save_csv(data, "results.csv")
```

## Project Structure

```
python-scraper/
+-- __init__.py        # Package entry-point
+-- scraper.py         # Core scraping logic and CLI
+-- requirements.txt   # Python dependencies
+-- README.md          # This file
```

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| requests | >= 2.31.0 | HTTP client |
| beautifulsoup4 | >= 4.12.0 | HTML parsing |
| lxml | >= 4.9.0 | Fast HTML parser backend |
