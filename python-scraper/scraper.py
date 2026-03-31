"""
Web scraper module that extracts page titles, links, and headers from a given URL.

This module provides a Python equivalent of the Go-based web scraper in the
``scraper/`` directory. It uses ``requests`` for HTTP fetching and
``BeautifulSoup`` for HTML parsing, and outputs results either as formatted
plain text or as JSON.

Example:
    Basic usage from the command line::

        python scraper.py --url https://example.com

    JSON output::

        python scraper.py --url https://example.com --json
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict, dataclass, field
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Logging
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
    """Container for data extracted from a single web page.

    Attributes:
        url: The URL that was scraped.
        title: The text content of the page ``<title>`` element.
        links: All non-anchor ``href`` values found on the page.
        headers: Text content of all ``h1``, ``h2``, and ``h3`` elements.
    """

    url: str
    title: str = ""
    links: list[str] = field(default_factory=list)
    headers: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Core scraping logic
# ---------------------------------------------------------------------------


def scrape(url: str, timeout: int = 10) -> Optional[ScrapedData]:
    """Fetch *url* and extract its title, links, and headers.

    Args:
        url: Fully-qualified URL to scrape (e.g. ``https://example.com``).
        timeout: HTTP request timeout in seconds. Defaults to ``10``.

    Returns:
        A :class:`ScrapedData` instance populated with the extracted content,
        or ``None`` if the request fails.

    Raises:
        requests.exceptions.MissingSchema: If *url* has no scheme.

    Example:
        >>> data = scrape("https://example.com")
        >>> data.title
        'Example Domain'
    """
    logger.info("Visiting: %s", url)

    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "python-scraper/1.0"},
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logger.error("Error fetching %s: %s", url, exc)
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    data = ScrapedData(url=url)

    # ---- Title ----------------------------------------------------------- #
    title_tag = soup.find("title")
    if title_tag:
        data.title = title_tag.get_text(strip=True)

    # ---- Links ----------------------------------------------------------- #
    for anchor in soup.find_all("a", href=True):
        href: str = anchor["href"].strip()
        # Skip pure fragment links (mirrors Go scraper behaviour)
        if not href or href.startswith("#"):
            continue
        # Resolve relative URLs against the page origin
        absolute = _resolve_url(base=url, href=href)
        if absolute:
            data.links.append(absolute)

    # ---- Headers (h1 / h2 / h3) ----------------------------------------- #
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            data.headers.append(text)

    return data


def _resolve_url(base: str, href: str) -> Optional[str]:
    """Resolve *href* relative to *base*, returning an absolute URL.

    Args:
        base: The URL of the page being scraped.
        href: The raw ``href`` attribute value to resolve.

    Returns:
        An absolute URL string, or ``None`` if *href* cannot be resolved
        (e.g. ``mailto:`` or ``javascript:`` pseudo-links).

    Example:
        >>> _resolve_url("https://example.com/page", "/about")
        'https://example.com/about'
    """
    # Pass through already-absolute URLs
    parsed = urlparse(href)
    if parsed.scheme in ("mailto", "javascript", "tel", "data"):
        return None
    if parsed.scheme:
        return href
    # urljoin handles relative paths, root-relative paths ("/foo"), and
    # protocol-relative URLs ("//host/path") correctly.
    return urljoin(base, href)


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

_PREVIEW_LIMIT = 10  # Number of items shown before "... and N more" truncation


def print_results(data: ScrapedData) -> None:
    """Print *data* as a human-readable report to stdout.

    The output format intentionally mirrors the plain-text output of the Go
    scraper for consistency.

    Args:
        data: The :class:`ScrapedData` instance to display.
    """
    print("=== Scrape Results ===")
    print(f"URL: {data.url}")
    print(f"Title: {data.title}")

    print("\n--- Headers ---")
    _print_list(data.headers)

    print("\n--- Links ---")
    _print_list(data.links)


def _print_list(items: list[str]) -> None:
    """Print up to :data:`_PREVIEW_LIMIT` items, then a summary line.

    Args:
        items: Sequence of strings to display.
    """
    for i, item in enumerate(items):
        if i >= _PREVIEW_LIMIT:
            remaining = len(items) - _PREVIEW_LIMIT
            print(f"... and {remaining} more")
            break
        print(f"- {item}")


def to_json(data: ScrapedData, indent: int = 2) -> str:
    """Serialize *data* to a JSON string.

    Args:
        data: The :class:`ScrapedData` instance to serialize.
        indent: JSON indentation width. Defaults to ``2``.

    Returns:
        A pretty-printed JSON string.

    Example:
        >>> import json
        >>> data = ScrapedData(url="https://example.com", title="Example")
        >>> parsed = json.loads(to_json(data))
        >>> parsed["title"]
        'Example'
    """
    return json.dumps(asdict(data), indent=indent)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _build_arg_parser() -> argparse.ArgumentParser:
    """Construct and return the CLI argument parser.

    Returns:
        A configured :class:`argparse.ArgumentParser` instance.
    """
    parser = argparse.ArgumentParser(
        description="Scrape a URL and extract its title, links, and headers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scraper.py --url https://example.com\n"
            "  python scraper.py --url https://example.com --json\n"
        ),
    )
    parser.add_argument(
        "--url",
        required=True,
        metavar="URL",
        help="Fully-qualified URL to scrape.",
    )
    parser.add_argument(
        "--json",
        dest="output_json",
        action="store_true",
        default=False,
        help="Output results as JSON instead of plain text.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        metavar="SECONDS",
        help="HTTP request timeout in seconds (default: 10).",
    )
    return parser


def main() -> None:
    """Parse CLI arguments and run the scraper.

    Exits with code ``1`` if the scrape fails (network error, bad status,
    etc.).
    """
    parser = _build_arg_parser()
    args = parser.parse_args()

    data = scrape(args.url, timeout=args.timeout)
    if data is None:
        logger.error("Scraping failed -- exiting.")
        sys.exit(1)

    if args.output_json:
        print(to_json(data))
    else:
        print_results(data)


if __name__ == "__main__":
    main()
