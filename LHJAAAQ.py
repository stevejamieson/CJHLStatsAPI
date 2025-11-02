from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.lhjaaaq.com/en/stats/player_standing.html?season=4650&subSeason=4652&category=1093")
    page.wait_for_selector("table")  # Wait for the table to load

    soup = BeautifulSoup(page.content(), "html.parser")
    skaters = []

    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        if len(cols) >= 10:
            skaters.append({
                "name": cols[1].text.strip(),
                "position": cols[3].text.strip(),
                "team": cols[2].text.strip(),
                "GP": cols[4].text.strip(),
                "G": cols[5].text.strip(),
                "A": cols[6].text.strip(),
                "Points": cols[7].text.strip(),

            })

    browser.close()

print(skaters)
