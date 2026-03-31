# test-playground

A collection of small web-scraper implementations in different languages.

## Projects

| Directory          | Language | Description                                      |
|--------------------|----------|--------------------------------------------------|
| [`scraper/`](scraper/)               | Go       | Web scraper using [Colly](https://github.com/gocolly/colly) |
| [`python-scraper/`](python-scraper/) | Python   | Web scraper using [requests](https://requests.readthedocs.io/) + [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) |

## Quick start

### Go scraper

```bash
cd scraper
go mod tidy
go run main.go -url https://example.com
```

### Python scraper

```bash
cd python-scraper
pip install -r requirements.txt
python scraper.py --url https://example.com
```

See each sub-directory's `README.md` for full documentation.
