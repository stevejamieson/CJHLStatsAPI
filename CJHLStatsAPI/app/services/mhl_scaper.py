from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from app.models import PlayerStats

def scrape_mhl_stats() -> list[PlayerStats]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.themhl.ca/stats/player-stats")
        page.wait_for_selector("table")
        soup = BeautifulSoup(page.content(), "html.parser")
        players = []
        for row in soup.select("table tbody tr"):
            cols = row.find_all("td")
            if len(cols) >= 12:
                players.append(PlayerStats(
                    name=cols[3].text.strip(),
                    position=cols[5].text.strip(),
                    team=cols[6].text.strip(),
                    GP=int(cols[7].text.strip()),
                    G=int(cols[8].text.strip()),
                    A=int(cols[9].text.strip()),
                    Points=int(cols[10].text.strip()),
                ))
        browser.close()
        return players
