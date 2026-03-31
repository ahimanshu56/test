"""
Python Web Scraper

A web scraper built with BeautifulSoup and requests that mirrors the functionality
of the companion Go scraper (scraper/main.go), while adding additional capabilities
such as metadata extraction, image scraping, and CSV export.

Usage:
    python scraper.py --url https://example.com
    python scraper.py --url https://example.com --json
    python scraper.py --url https://example.com --output results.json
    python scraper.py --url https://example.com --csv results.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from dataclasses import asdict, dataclass, field
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class ScrapedData:
    """Container for all data extracted from a single web page.

    Attributes:
        url: The URL that was scraped.
        title: The page ``<title>`` text, or an empty string if not found.
        links: All absolute hyperlinks found on the page (``<a href>``).
        headers: Text content of every ``<h1>``, ``<h2>``, and ``<h3>`` element.
        meta_description: Content of the ``<meta name=\"description\">`` tag.
        meta_keywords: Content of the ``<meta name=\"keywords\">`` tag.
        images: Absolute URLs of all ``<img src>`` elements.
        status_code: HTTP status code returned by the server.
    """

    url: str
    title: str = ""
    links: list[str] = field(default_factory=list)
    headers: list[str] = field(default_factory=list)
    meta_description: str = ""
    meta_keywords: str = ""
    images: list[str] = field(default_factory=list)
    status_code: int = 0

    def to_dict(self) -> dict:
        """Return a plain-dictionary representation of the scraped data.

        Returns:
            A dictionary with the same fields as this dataclass.
        """
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        """Serialise the scraped data to a JSON string.

        Args:
            indent: Number of spaces used for JSON indentation.

        Returns:
            Pretty-printed JSON string.
        """
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Core scraping logic
# ---------------------------------------------------------------------------


def scrape(
    url: str,
    timeout: int = 10,
    user_agent: Optional[str] = None,
) -> ScrapedData:
    """Fetch *url* and extract structured data from the HTML response.

    Mirrors the ``scrape()`` function in ``scraper/main.go`` and adds:

    * ``<meta>`` description and keywords extraction
    * Image URL collection
    * HTTP status-code recording
    * Relative-to-absolute link and image URL resolution

    Args:
        url: Fully-qualified URL to scrape (e.g. ``https://example.com``).
        timeout: Request timeout in seconds. Defaults to ``10``.
        user_agent: Custom ``User-Agent`` header value. When ``None`` a
            descriptive default is used.

    Returns:
        A :class:`ScrapedData` instance populated with the page contents.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails
            (connection error, timeout, invalid URL, etc.).
    """
    if user_agent is None:
        user_agent = (
            "Mozilla/5.0 (compatible; python-scraper/1.0; "
            "+https://github.com/patelraj0602/test-playground)"
        )

    headers = {"User-Agent": user_agent}

    logger.info("Visiting: %s", url)
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()

    data = ScrapedData(url=url, status_code=response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    # --- Title -----------------------------------------------------------
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        data.title = title_tag.string.strip()

    # --- Meta tags -------------------------------------------------------
    desc_tag = soup.find("meta", attrs={"name": "description"})
    if desc_tag and desc_tag.get("content"):
        data.meta_description = str(desc_tag["content"]).strip()

    kw_tag = soup.find("meta", attrs={"name": "keywords"})
    if kw_tag and kw_tag.get("content"):
        data.meta_keywords = str(kw_tag["content"]).strip()

    # --- Links -----------------------------------------------------------
    base = _base_url(url)
    for a_tag in soup.find_all("a", href=True):
        href: str = a_tag["href"].strip()
        if not href or href.startswith("#"):
            continue
        absolute = urljoin(base, href)
        data.links.append(absolute)

    # --- Headers (h1 / h2 / h3) -----------------------------------------
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(separator=" ", strip=True)
        if text:
            data.headers.append(text)

    # --- Images ----------------------------------------------------------
    for img_tag in soup.find_all("img", src=True):
        src: str = img_tag["src"].strip()
        if src:
            data.images.append(urljoin(base, src))

    return data


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def print_results(data: ScrapedData, max_items: int = 10) -> None:
    """Print a human-readable summary of *data* to stdout.

    Mirrors the ``printResults()`` function in ``scraper/main.go``.

    Args:
        data: The scraped data to display.
        max_items: Maximum number of items to show per list before
            printing a "... and N more" continuation line. Defaults to ``10``.
    """

    def _print_list(label: str, items: list[str]) -> None:
        print(f"\n--- {label} ---")
        for i, item in enumerate(items):
            if i >= max_items:
                print(f"... and {len(items) - max_items} more")
                break
            print(f"  - {item}")

    print("=== Scrape Results ===")
    print(f"URL:    {data.url}")
    print(f"Status: {data.status_code}")
    print(f"Title:  {data.title}")

    if data.meta_description:
        print(f"Meta Description: {data.meta_description}")
    if data.meta_keywords:
        print(f"Meta Keywords:    {data.meta_keywords}")

    _print_list("Headers", data.headers)
    _print_list("Links", data.links)
    _print_list("Images", data.images)


def save_json(data: ScrapedData, path: str) -> None:
    """Write scraped data to a JSON file.

    Args:
        data: The scraped data to serialise.
        path: Destination file path. The file is created or overwritten.

    Raises:
        OSError: If the file cannot be written.
    """
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(data.to_json())
    logger.info("JSON output written to: %s", path)


def save_csv(data: ScrapedData, path: str) -> None:
    """Write scraped data to a CSV file.

    Each row represents a single extracted item (link, header, or image).
    The CSV has columns: ``type``, ``value``.

    Args:
        data: The scraped data to serialise.
        path: Destination file path. The file is created or overwritten.

    Raises:
        OSError: If the file cannot be written.
    """
    rows: list[dict[str, str]] = []
    rows.append({"type": "url", "value": data.url})
    rows.append({"type": "title", "value": data.title})
    rows.append({"type": "status_code", "value": str(data.status_code)})
    rows.append({"type": "meta_description", "value": data.meta_description})
    rows.append({"type": "meta_keywords", "value": data.meta_keywords})
    for h in data.headers:
        rows.append({"type": "header", "value": h})
    for link in data.links:
        rows.append({"type": "link", "value": link})
    for img in data.images:
        rows.append({"type": "image", "value": img})

    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["type", "value"])
        writer.writeheader()
        writer.writerows(rows)
    logger.info("CSV output written to: %s", path)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _base_url(url: str) -> str:
    """Return the scheme + netloc portion of *url* for resolving relative links.

    Args:
        url: Any fully-qualified URL.

    Returns:
        String of the form ``scheme://netloc`` (e.g. ``https://example.com``).
    """
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


# ---------------------------------------------------------------------------
# CLI entry-point
# ---------------------------------------------------------------------------


def _build_arg_parser() -> argparse.ArgumentParser:
    """Construct and return the CLI argument parser.

    Returns:
        Configured :class:`argparse.ArgumentParser` instance.
    """
    parser = argparse.ArgumentParser(
        prog="scraper",
        description=(
            "Python web scraper - extracts title, headers, links, images, "
            "and meta tags from a URL."
        ),
    )
    parser.add_argument(
        "--url",
        required=True,
        metavar="URL",
        help="URL to scrape (e.g. https://example.com).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        default=False,
        help="Print results as JSON to stdout.",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        default=None,
        help="Save results as JSON to FILE.",
    )
    parser.add_argument(
        "--csv",
        metavar="FILE",
        default=None,
        dest="csv_output",
        help="Save results as CSV to FILE.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        metavar="SECONDS",
        help="HTTP request timeout in seconds (default: 10).",
    )
    parser.add_argument(
        "--user-agent",
        metavar="STRING",
        default=None,
        help="Custom User-Agent header value.",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    """Parse CLI arguments, run the scraper, and write output.

    Args:
        argv: Argument list to parse. When ``None``, :data:`sys.argv` is used
            (the standard behaviour for a CLI entry-point).

    Returns:
        Exit code: ``0`` on success, ``1`` on error.
    """
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    try:
        data = scrape(
            url=args.url,
            timeout=args.timeout,
            user_agent=args.user_agent,
        )
    except requests.exceptions.RequestException as exc:
        logger.error("Failed to scrape %s: %s", args.url, exc)
        return 1

    # Stdout output
    if args.json:
        print(data.to_json())
    else:
        print_results(data)

    # File output
    if args.output:
        try:
            save_json(data, args.output)
        except OSError as exc:
            logger.error("Could not write JSON output: %s", exc)
            return 1

    if args.csv_output:
        try:
            save_csv(data, args.csv_output)
        except OSError as exc:
            logger.error("Could not write CSV output: %s", exc)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
