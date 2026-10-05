# 📚 CodeAlpha Web Scraping Project

A production-grade Python web scraper that extracts book data from
[books.toscrape.com](https://books.toscrape.com) and produces a clean,
analysis-ready dataset.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🎯 Features

- ✅ **Layered architecture** (fetch → parse → store)
- ✅ **Automatic retry** with exponential backoff
- ✅ **Structured logging** to file + console
- ✅ **Row-level validation** (rejects bad data)
- ✅ **Deduplication** by product URL
- ✅ **Multi-format output** (CSV + JSON)
- ✅ **Unit tests** with pytest
- ✅ **Ethical scraping** (User-Agent, delays, timeouts)

---

## 📁 Project Structure

```
CodeAlpha_Webscraping/
├── src/               # Source modules
├── data/              # Output datasets
├── logs/              # Runtime logs
├── tests/             # Unit tests
├── main.py            # Entry point
└── requirements.txt
```

---

## 🚀 Quick Start

```bash
# 1. Clone & enter
git clone <your-repo-url>
cd CodeAlpha_Webscraping

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the scraper
python main.py                 # default: 5 pages
python main.py 10              # scrape 10 pages
```

---

## 📊 Output Example

| title | price_gbp | rating | in_stock | price_inr |
|-------|-----------|--------|----------|-----------|
| A Light in the Attic | 51.77 | 3 | True | 5435.85 |
| Tipping the Velvet | 53.74 | 1 | True | 5642.70 |

**Outputs:**
- `data/books_dataset.csv` — analysis-ready dataset
- `data/books_dataset.json` — same data in JSON
- `logs/scraper.log` — full run history

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🛡️ Ethical Scraping

- ✅ Respects `robots.txt`
- ✅ Sends descriptive User-Agent
- ✅ 1-second delay between requests
- ✅ 30-second timeout + retries
- ✅ Targets a site explicitly built for scraping practice

---

## 📜 License

MIT — free for educational use.