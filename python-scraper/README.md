# Python Web Scraper

A Python web scraper that extracts page titles, links, and headers from a given
URL. This is a feature-equivalent Python port of the Go scraper in the
[`scraper/`](../scraper/) directory, using
[`requests`](https://requests.readthedocs.io/) and
[`BeautifulSoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Features

- Scrape page title
- Extract all links from a page (relative links are resolved to absolute URLs)
- Extract headers (h1, h2, h3)
- Skip fragment (`#`) links and pseudo-links (`mailto:`, `javascript:`, etc.)
- Output as plain text **or** JSON
- Type-annotated, Google-style docstrings throughout

## Requirements

- Python 3.10+
- See [`requirements.txt`](requirements.txt) for library dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage

```bash
python scraper.py --url https://example.com
```

### JSON output

```bash
python scraper.py --url https://example.com --json
```

### Custom timeout

```bash
python scraper.py --url https://example.com --timeout 30
```

### Full option reference

```
usage: scraper.py [-h] --url URL [--json] [--timeout SECONDS]

Scrape a URL and extract its title, links, and headers.

options:
  -h, --help         show this help message and exit
  --url URL          Fully-qualified URL to scrape.
  --json             Output results as JSON instead of plain text.
  --timeout SECONDS  HTTP request timeout in seconds (default: 10).
```

## Example Output

### Plain text

```
=== Scrape Results ===
URL: https://example.com
Title: Example Domain

--- Headers ---
- Example Domain

--- Links ---
- https://www.iana.org/domains/example
```

### JSON

```json
{
  "url": "https://example.com",
  "title": "Example Domain",
  "links": [
    "https://www.iana.org/domains/example"
  ],
  "headers": [
    "Example Domain"
  ]
}
```

## Programmatic usage

```python
from scraper import scrape, to_json

data = scrape("https://example.com")
if data:
    print(data.title)          # "Example Domain"
    print(data.links)          # ['https://www.iana.org/domains/example']
    print(to_json(data))       # pretty-printed JSON string
```

## Running the tests

```bash
pip install pytest
pytest tests/ -v
```

## Project layout

```
python-scraper/
├── scraper.py          # Main module – scraping logic and CLI entry point
├── __init__.py         # Package marker
├── conftest.py         # pytest path configuration
├── requirements.txt    # Runtime dependencies
├── README.md           # This file
└── tests/
    ├── __init__.py
    └── test_scraper.py # 19 unit tests (no network calls)
```

## Dependencies

| Package          | Version   | Purpose                    |
|------------------|-----------|----------------------------|
| `requests`       | ≥ 2.31.0  | HTTP fetching              |
| `beautifulsoup4` | ≥ 4.12.0  | HTML parsing               |
| `pytest`         | any       | Test runner (dev only)     |
