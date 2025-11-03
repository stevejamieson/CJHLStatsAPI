# 🏒 CJHLStatsAPI

A modular Python-based scraper for public Junior A hockey league sites across Canada. This project extracts player and team statistics from CJHL-affiliated leagues and exposes the data via a FastAPI backend.

---

## 📍 Target Leagues

This scraper supports the following CJHL leagues:

- **MHL** – Maritime Hockey League  
- **LHJAAAQ** – Quebec Junior AAA Hockey League  
- **CCHL** – Central Canada Hockey League  
- **OJHL** – Ontario Junior Hockey League  
- **NOJHL** – Northern Ontario Junior Hockey League  
- **SIJHL** – Superior International Junior Hockey League  
- **MJHL** – Manitoba Junior Hockey League  
- **SJHL** – Saskatchewan Junior Hockey League  
- **AJHL** – Alberta Junior Hockey League  

Reference: [CJHL Statistics Portal](https://www.cjhlhockey.com/en/statistics)

---

## 🧰 Tech Stack

| Layer         | Tools Used                          |
|---------------|-------------------------------------|
| Scraping      | `requests`, `BeautifulSoup`, `Playwright` |
| Backend API   | `FastAPI`                          |
| datalayer     | `Pydantic`                          |

---

---
## 🧰 Pydantic  Data Schema

Structured player statistics include:

| detail        |  Used                               |
|---------------|-------------------------------------|
| name      | `Player Name`                           |
| team      | `Team`                                  |
| Position  | `Position`                              |
| GP   | `Games Played`                               |
| G   | `Goals`                                       |
| A   | `Assists`                                     |
| P   | `Points`                                      |



---

## 🔄 Workflow Overview

1. **Scrape** player stats from public league sites.
2. **Normalize** structure and clean data for consistency across leagues.
3. **Expose** via FastAPI endpoints for dashboards or analytics.

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload

# Test MHL end point
http://localhost:8000/stats/mhl

GET /stats/mhl
[
  {
    "name": "Jack Hayne",
    "position": "C",
    "team": "CHA",
    "GP": 18,
    "G": 9,
    "A": 20,
    "Points": 29
  },
  {
    "name": "Ben Cross",
    "position": "LW",
    "team": "CHA",
    "GP": 17,
    "G": 15,
    "A": 11,
    "Points": 26
  },
  {
    "name": "Simon Mullen",
    "position": "D",
    "team": "SWC",
    "GP": 15,
    "G": 4,
    "A": 21,
    "Points": 25
  },
  {
    "name": "Coen Miller",
    "position": "LW",
    "team": "SWC",
    "GP": 13,
    "G": 12,
    "A": 12,
    "Points": 24
  },
  {
    "name": "Natan Grenier",
    "position": "D",
    "team": "WKS",
    "GP": 17,
    "G": 6,
    "A": 18,
    "Points": 24
  }
  // ...additional players omitted for brevity
]


