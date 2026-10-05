"""Handles saving scraped data to disk (CSV + JSON)."""

import json

import pandas as pd

from src.config import CSV_OUTPUT, DATA_DIR
from src.utils import setup_logger

logger = setup_logger(__name__)


def save_to_csv(rows: list[dict], path=CSV_OUTPUT) -> pd.DataFrame:
    """Save rows to CSV and return the DataFrame."""
    if not rows:
        logger.warning("No rows to save.")
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df.drop_duplicates(subset=["product_url"], inplace=True)
    df.sort_values("title", inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(path, index=False, encoding="utf-8")
    logger.info(f"Saved {len(df)} rows → {path}")
    return df


def save_to_json(rows: list[dict], filename: str = "books_dataset.json") -> None:
    """Save rows to a JSON file (bonus format)."""
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved {len(rows)} rows → {path}")