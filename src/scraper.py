"""Handles all HTTP requests to the target website."""

import requests

from src.config import BASE_URL, HEADERS, MAX_RETRIES, REQUEST_TIMEOUT, RETRY_DELAY
from src.utils import retry, setup_logger

logger = setup_logger(__name__)


@retry(max_attempts=MAX_RETRIES, delay=RETRY_DELAY)
def fetch_page(page_num: int) -> str:
    """Fetch raw HTML for a given page number. Retries on failure."""
    url = BASE_URL.format(page_num)
    logger.info(f"Fetching page {page_num}: {url}")

    response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    logger.info(f"Page {page_num} fetched ({len(response.text):,} bytes)")
    return response.text