"""Unit tests for the python-scraper module.

Tests use ``unittest.mock`` to avoid real HTTP calls and focus on verifying
the parsing logic, URL resolution, and output formatting.
"""

from __future__ import annotations

import json
import textwrap
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

import sys
import os

# Allow running tests from the python-scraper directory directly.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import (  # noqa: E402
    ScrapedData,
    _print_list,
    _resolve_url,
    print_results,
    scrape,
    to_json,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_SIMPLE_HTML = textwrap.dedent(
    """
    <html>
      <head><title>  Test Page  </title></head>
      <body>
        <h1>Main Heading</h1>
        <h2>Sub Heading</h2>
        <a href="https://example.com/page">External</a>
        <a href="/relative">Relative</a>
        <a href="#anchor">Anchor</a>
        <a href="mailto:foo@bar.com">Mail</a>
      </body>
    </html>
    """
)


def _mock_response(html: str, status_code: int = 200) -> MagicMock:
    """Return a mock :class:`requests.Response` with *html* as body."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = html
    resp.raise_for_status = MagicMock()
    return resp


# ---------------------------------------------------------------------------
# Tests: scrape()
# ---------------------------------------------------------------------------


class TestScrape(unittest.TestCase):
    """Tests for the :func:`scrape` function."""

    @patch("scraper.requests.get")
    def test_extracts_title(self, mock_get: MagicMock) -> None:
        """Title whitespace is stripped."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        data = scrape("https://base.com/")
        self.assertEqual(data.title, "Test Page")

    @patch("scraper.requests.get")
    def test_extracts_headers(self, mock_get: MagicMock) -> None:
        """h1 and h2 text is collected."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        data = scrape("https://base.com/")
        self.assertIn("Main Heading", data.headers)
        self.assertIn("Sub Heading", data.headers)

    @patch("scraper.requests.get")
    def test_skips_anchor_links(self, mock_get: MagicMock) -> None:
        """Pure fragment ``#...`` links are excluded."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        data = scrape("https://base.com/")
        self.assertNotIn("#anchor", data.links)

    @patch("scraper.requests.get")
    def test_skips_mailto_links(self, mock_get: MagicMock) -> None:
        """``mailto:`` links are excluded."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        data = scrape("https://base.com/")
        for link in data.links:
            self.assertFalse(link.startswith("mailto:"), link)

    @patch("scraper.requests.get")
    def test_resolves_relative_links(self, mock_get: MagicMock) -> None:
        """Relative hrefs are converted to absolute URLs."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        data = scrape("https://base.com/")
        self.assertIn("https://base.com/relative", data.links)

    @patch("scraper.requests.get")
    def test_returns_none_on_request_error(self, mock_get: MagicMock) -> None:
        """``None`` is returned when the HTTP request raises an exception."""
        import requests as req

        mock_get.side_effect = req.exceptions.ConnectionError("network down")
        data = scrape("https://unreachable.invalid/")
        self.assertIsNone(data)

    @patch("scraper.requests.get")
    def test_url_stored_on_data(self, mock_get: MagicMock) -> None:
        """The scraped URL is preserved on the returned object."""
        mock_get.return_value = _mock_response(_SIMPLE_HTML)
        url = "https://base.com/foo"
        data = scrape(url)
        self.assertEqual(data.url, url)


# ---------------------------------------------------------------------------
# Tests: _resolve_url()
# ---------------------------------------------------------------------------


class TestResolveUrl(unittest.TestCase):
    """Tests for the :func:`_resolve_url` helper."""

    def test_absolute_passthrough(self) -> None:
        result = _resolve_url("https://example.com/", "https://other.com/page")
        self.assertEqual(result, "https://other.com/page")

    def test_root_relative(self) -> None:
        result = _resolve_url("https://example.com/path/page", "/about")
        self.assertEqual(result, "https://example.com/about")

    def test_relative_path(self) -> None:
        result = _resolve_url("https://example.com/dir/page", "sub/resource")
        self.assertEqual(result, "https://example.com/dir/sub/resource")

    def test_mailto_returns_none(self) -> None:
        result = _resolve_url("https://example.com/", "mailto:foo@bar.com")
        self.assertIsNone(result)

    def test_javascript_returns_none(self) -> None:
        result = _resolve_url("https://example.com/", "javascript:void(0)")
        self.assertIsNone(result)

    def test_protocol_relative(self) -> None:
        result = _resolve_url("https://example.com/", "//cdn.example.com/js")
        self.assertEqual(result, "https://cdn.example.com/js")


# ---------------------------------------------------------------------------
# Tests: to_json()
# ---------------------------------------------------------------------------


class TestToJson(unittest.TestCase):
    """Tests for the :func:`to_json` serialiser."""

    def _make_data(self) -> ScrapedData:
        return ScrapedData(
            url="https://example.com",
            title="Example",
            links=["https://example.com/a"],
            headers=["Heading"],
        )

    def test_valid_json(self) -> None:
        """Output is valid JSON."""
        result = to_json(self._make_data())
        parsed = json.loads(result)
        self.assertIsInstance(parsed, dict)

    def test_fields_present(self) -> None:
        """All four fields are present in the serialised output."""
        parsed = json.loads(to_json(self._make_data()))
        for key in ("url", "title", "links", "headers"):
            self.assertIn(key, parsed)

    def test_values_round_trip(self) -> None:
        """Values survive a JSON round-trip unchanged."""
        data = self._make_data()
        parsed = json.loads(to_json(data))
        self.assertEqual(parsed["url"], data.url)
        self.assertEqual(parsed["title"], data.title)
        self.assertEqual(parsed["links"], data.links)
        self.assertEqual(parsed["headers"], data.headers)


# ---------------------------------------------------------------------------
# Tests: print_results() / _print_list()
# ---------------------------------------------------------------------------


class TestPrintResults(unittest.TestCase):
    """Tests for the plain-text output helpers."""

    def _capture_print_results(self, data: ScrapedData) -> str:
        buf = StringIO()
        with patch("sys.stdout", buf):
            print_results(data)
        return buf.getvalue()

    def test_contains_url(self) -> None:
        data = ScrapedData(url="https://example.com", title="T")
        output = self._capture_print_results(data)
        self.assertIn("https://example.com", output)

    def test_contains_title(self) -> None:
        data = ScrapedData(url="https://example.com", title="My Title")
        output = self._capture_print_results(data)
        self.assertIn("My Title", output)

    def test_truncates_long_lists(self) -> None:
        """Lists longer than 10 items show a '... and N more' suffix."""
        buf = StringIO()
        items = [f"item-{i}" for i in range(15)]
        with patch("sys.stdout", buf):
            _print_list(items)
        output = buf.getvalue()
        self.assertIn("and 5 more", output)
        self.assertNotIn("item-10", output)


if __name__ == "__main__":
    unittest.main()
