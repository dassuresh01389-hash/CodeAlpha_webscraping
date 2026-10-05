"""
CodeAlpha Internship — Web Scraping Project
Entry point: orchestrates fetch → parse → save pipeline.
"""

import sys
import time
from datetime import datetime

from src.config import MAX_PAGES, POLITE_DELAY
from src.parser import parse_page
from src.scraper import fetch_page
from src.storage import save_to_csv, save_to_json
from src.utils import setup_logger

logger = setup_logger("main")


def run(max_pages: int = MAX_PAGES) -> None:
    """Main pipeline."""
    start = datetime.now()
    logger.info("=" * 60)
    logger.info("CodeAlpha Web Scraping Project — START")
    logger.info(f"Target pages: {max_pages}")
    logger.info("=" * 60)

    all_books = []

    for page in range(1, max_pages + 1):
        try:
            html = fetch_page(page)
            books = parse_page(html, page)
            all_books.extend(books)
            logger.info(f"Running total: {len(all_books)} books")
        except Exception as e:
            logger.error(f"Page {page} failed permanently: {e}")
            continue
        time.sleep(POLITE_DELAY)

    # Save results
    df = save_to_csv(all_books)
    save_to_json(all_books)

    # Report
    duration = (datetime.now() - start).total_seconds()
    logger.info("=" * 60)
    logger.info(f"✓ Scraped {len(all_books)} books in {duration:.1f}s")
    logger.info(f"✓ Unique books: {len(df)}")
    if not df.empty:
        logger.info(f"✓ Avg price: £{df['price_gbp'].mean():.2f}")
        logger.info(f"✓ Rating distribution: {df['rating'].value_counts().to_dict()}")
    logger.info("=" * 60)


if __name__ == "__main__":
    pages = int(sys.argv[1]) if len(sys.argv) > 1 else MAX_PAGES
    run(max_pages=pages)