"""
python-scraper
==============

A Python web scraper that extracts structured data from web pages.

Mirrors the companion Go scraper (``scraper/main.go``) and adds extra
capabilities:

* ``<meta>`` description and keywords extraction
* Image URL collection
* HTTP status-code recording
* JSON and CSV export
* Importable as a library

Quick start::

    from python_scraper.scraper import scrape, print_results

    data = scrape("https://example.com")
    print_results(data)
"""

from .scraper import ScrapedData, scrape, print_results, save_csv, save_json

__all__ = [
    "ScrapedData",
    "scrape",
    "print_results",
    "save_csv",
    "save_json",
]
