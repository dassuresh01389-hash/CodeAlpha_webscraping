"""Utility helpers: logging, retry, validation."""

import logging
import time
from functools import wraps

from src.config import LOG_FILE


def setup_logger(name: str = "scraper") -> logging.Logger:
    """Configure a logger that writes to file and console."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    return logger


def retry(max_attempts: int = 3, delay: int = 3, backoff: float = 2.0):
    """Decorator: retry a function on exception with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wait = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    logging.warning(
                        f"{func.__name__} attempt {attempt}/{max_attempts} "
                        f"failed: {e}. Retrying in {wait}s..."
                    )
                    time.sleep(wait)
                    wait *= backoff
        return wrapper
    return decorator


def validate_row(row: dict) -> list[str]:
    """Return list of validation errors for a scraped row."""
    errors = []
    if not row.get("title") or len(row["title"]) < 2:
        errors.append("invalid title")
    if not isinstance(row.get("price_gbp"), (int, float)):
        errors.append("invalid price")
    elif not (0 < row["price_gbp"] < 10_000):
        errors.append("price out of range")
    if row.get("rating") not in {1, 2, 3, 4, 5}:
        errors.append("invalid rating")
    if not row.get("product_url", "").startswith("http"):
        errors.append("invalid URL")
    return errors