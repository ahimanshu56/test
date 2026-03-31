# conftest.py — pytest configuration for python-scraper
# Ensures the package root is on sys.path so tests can import scraper directly.
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
