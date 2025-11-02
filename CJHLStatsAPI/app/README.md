# 🏒 Junior A Hockey Stats Scraper

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


---

---

## 🧰 Pydantic  Object Modeling 

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

1. **Scrape** player and team stats from public league sites.
2. **Normalize** and clean data for consistency across leagues.
3. **Expose** via FastAPI endpoints for dashboards or analytics.

---

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload

# Test MHL end points
http://localhost:8000/stats/mhl
