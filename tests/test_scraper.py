"""Unit tests for the scraper project."""

import pandas as pd
import pytest

from src.parser import parse_page
from src.config import CSV_OUTPUT


SAMPLE_HTML = """
<article class="product_pod">
  <h3><a title="Test Book" href="test-book/index.html">Test</a></h3>
  <p class="price_color">£19.99</p>
  <p class="star-rating Four"></p>
  <p class="instock availability">In stock</p>
</article>
"""


def test_parse_single_book():
    books = parse_page(SAMPLE_HTML, page_num=1)
    assert len(books) == 1
    book = books[0]
    assert book["title"] == "Test Book"
    assert book["price_gbp"] == 19.99
    assert book["rating"] == 4
    assert book["in_stock"] is True


def test_csv_exists_and_valid():
    df = pd.read_csv(CSV_OUTPUT)
    assert len(df) > 0
    assert df["price_gbp"].between(1, 1000).all()
    assert df["rating"].isin([1, 2, 3, 4, 5]).all()
    assert df["product_url"].str.startswith("http").all()
    assert df.duplicated(subset=["product_url"]).sum() == 0


def test_no_missing_values():
    df = pd.read_csv(CSV_OUTPUT)
    assert df.isnull().sum().sum() == 0