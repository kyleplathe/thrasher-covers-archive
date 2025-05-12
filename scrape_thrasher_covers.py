import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
from datetime import datetime
import json
import re

BASE_URL = "https://www.thrashermagazine.com"
COVERS_PAGE = f"{BASE_URL}/covers/"

def format_cover_url(date, src):
    """Format the cover URL based on the date and source URL."""
    year = date.year
    month = date.month
    
    # For recent covers (2021 onwards)
    if year >= 2021:
        return urljoin(BASE_URL, src)
    
    # For 2019-2020 covers
    elif year >= 2019:
        month_str = str(month).zfill(2)
        year_str = str(year)[-2:]  # Get last 2 digits of year
        return f"{BASE_URL}/images/TH{month_str}{year_str}Cover.jpg"
    
    # For 2018-2019 covers
    elif year >= 2018:
        month_name = date.strftime("%B")
        year_str = str(year)[-2:]
        path = f"/images/image/Covers Section/images/{month_name}{year_str}sfw.jpg"
        return BASE_URL + quote(path)
    
    # For older covers (1981-2017)
    else:
        month_name = date.strftime("%B")
        path = f"/images/image/Covers Section/images/{month_name}{year}.jpg"
        return BASE_URL + quote(path)

def scrape_covers():
    print("🛹 Scraping Thrasher covers archive...")
    response = requests.get(COVERS_PAGE)
    soup = BeautifulSoup(response.text, "html.parser")
    covers = []

    # Find all <img> tags with alt matching 'YYYY-MM-DD Cover'
    for img in soup.find_all("img"):
        alt = img.get("alt", "")
        src = img.get("src", "")
        match = re.match(r"(\d{4}-\d{2}-\d{2}) Cover", alt)
        if not match or not src:
            continue
        date_str = match.group(1)
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
        except Exception as e:
            print(f"⚠️ Error parsing date for {src}: {e}")
            continue

        # Format the URL based on the date
        full_url = format_cover_url(dt, src)

        covers.append({
            "year": dt.year,
            "month": dt.strftime("%B"),
            "url": full_url
        })
    print(f"✅ Scraped {len(covers)} covers and saved to covers.json")
    return covers

if __name__ == "__main__":
    data = scrape_covers()
    with open("covers.json", "w") as f:
        json.dump(data, f, indent=2)
