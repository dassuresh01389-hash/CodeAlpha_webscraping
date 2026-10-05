"""Configuration for the web scraping project."""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Scraping targets
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGES = 5
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 3
POLITE_DELAY = 1

# HTTP headers (identify your bot ethically)
HEADERS = {
    "User-Agent": (
        "CodeAlpha-Internship-Bot/1.0 "
        "(+https://github.com/yourusername/codealpha-webscraping; educational)"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# Rating mapping
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

# Currency conversion (approximate, for demo)
GBP_TO_INR = 105.0

# Output files
CSV_OUTPUT = DATA_DIR / "books_dataset.csv"
LOG_FILE = LOG_DIR / "scraper.log"