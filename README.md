# test-playground

A collection of web scraper implementations in multiple languages.

## Projects

### Go Scraper (`scraper/`)

A web scraper built in Go using the [Colly](https://github.com/gocolly/colly) library.

**Features:** page title, links, headers (h1/h2/h3), JSON output

```bash
cd scraper
go run main.go --url https://example.com
go run main.go --url https://example.com --json
```

See [scraper/README.md](scraper/README.md) for full documentation.

---

### Python Scraper (`python-scraper/`)

A web scraper built in Python using [Requests](https://docs.python-requests.org/)
and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/). Mirrors the
Go scraper and adds meta-tag extraction, image scraping, CSV export, and library usage.

**Features:** page title, links, headers (h1/h2/h3), meta tags, images, HTTP status,
JSON output, JSON/CSV file export, importable library

```bash
cd python-scraper
pip install -r requirements.txt
python scraper.py --url https://example.com
python scraper.py --url https://example.com --json
python scraper.py --url https://example.com --output results.json --csv results.csv
```

See [python-scraper/README.md](python-scraper/README.md) for full documentation.
