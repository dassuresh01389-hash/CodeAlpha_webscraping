"""Parses HTML and extracts structured book data."""

from bs4 import BeautifulSoup

from src.config import GBP_TO_INR, RATING_MAP
from src.utils import setup_logger, validate_row

logger = setup_logger(__name__)


def _clean_price(price_text: str) -> float:
    """Convert '£51.77' or 'Â£51.77' to 51.77."""
    return float(price_text.replace("£", "").replace("Â", "").strip())


def _extract_rating(rating_class: list[str]) -> int:
    """Convert ['star-rating', 'Three'] → 3."""
    words = [c for c in rating_class if c != "star-rating"]
    return RATING_MAP.get(words[0], 0) if words else 0


def parse_page(html: str, page_num: int) -> list[dict]:
    """Parse one page of HTML into a list of book dicts."""
    soup = BeautifulSoup(html, "lxml")
    articles = soup.select("article.product_pod")
    logger.info(f"Page {page_num}: found {len(articles)} book elements")

    books = []
    for idx, article in enumerate(articles, 1):
        try:
            title = article.h3.a["title"]
            price = _clean_price(article.select_one("p.price_color").text)
            rating = _extract_rating(article.select_one("p.star-rating")["class"])
            availability = article.select_one("p.instock.availability").text.strip()
            relative_url = article.h3.a["href"].replace("../", "")
            product_url = f"https://books.toscrape.com/catalogue/{relative_url}"

            row = {
                "title": title,
                "price_gbp": price,
                "rating": rating,
                "availability": availability,
                "product_url": product_url,
                "price_inr": round(price * GBP_TO_INR, 2),
                "in_stock": "In stock" in availability,
                "source_page": page_num,
            }

            errors = validate_row(row)
            if errors:
                logger.warning(f"Page {page_num} row {idx} invalid: {errors}")
                continue

            books.append(row)

        except (AttributeError, KeyError, ValueError) as e:
            logger.warning(f"Page {page_num} row {idx} parsing failed: {e}")
            continue

    return books