import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote
from datetime import datetime
import json
import re
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        base_pattern = f"{BASE_URL}/images/TH{month_str}{year_str}"
        # Try alternate extensions and suffixes
        for ext in [".jpg", ".jpeg", ".png"]:
            for suffix in ["", "Cover", "sfw"]:
                url = base_pattern + suffix + ext
                if verify_cover_url(url):
                    return url
        return base_pattern + "Cover.jpg"  # Default fallback
    
    # For 2018-2019 covers
    elif year >= 2018:
        month_name = date.strftime("%B")
        year_str = str(year)[-2:]
        base_pattern = f"{BASE_URL}/images/image/Covers%20Section/images/{month_name}{year_str}"
        # Try alternate extensions and suffixes
        for ext in [".jpg", ".jpeg", ".png"]:
            for suffix in ["", "sfw", "Cover"]:
                url = base_pattern + suffix + ext
                if verify_cover_url(url):
                    return url
        return base_pattern + "sfw.jpg"  # Default fallback
    
    # For older covers (1981-2017)
    else:
        month_name = date.strftime("%B")
        base_pattern = f"{BASE_URL}/images/image/Covers%20Section/images/{month_name}{year}"
        # Try alternate extensions and suffixes
        for ext in [".jpg", ".jpeg", ".png"]:
            for suffix in ["", "Cover", "sfw"]:
                url = base_pattern + suffix + ext
                if verify_cover_url(url):
                    return url
        return base_pattern + ".jpg"  # Default fallback

def verify_cover_url(url):
    """Verify if the cover URL is accessible."""
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Error verifying URL {url}: {e}")
        return False

def scrape_covers():
    logger.info("🛹 Scraping Thrasher covers archive...")
    response = requests.get(COVERS_PAGE)
    soup = BeautifulSoup(response.text, "html.parser")
    covers = []
    failed_covers = []

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
            logger.error(f"⚠️ Error parsing date for {src}: {e}")
            continue

        # Format the URL based on the date
        full_url = format_cover_url(dt, src)
        
        # Verify the URL is accessible
        if verify_cover_url(full_url):
            covers.append({
                "year": dt.year,
                "month": dt.strftime("%B"),
                "url": full_url
            })
        else:
            failed_covers.append({
                "date": date_str,
                "url": full_url
            })
            logger.warning(f"Failed to access cover for {date_str}: {full_url}")

    logger.info(f"✅ Successfully scraped {len(covers)} covers")
    if failed_covers:
        logger.warning(f"⚠️ Failed to scrape {len(failed_covers)} covers")
        with open("failed_covers.json", "w") as f:
            json.dump(failed_covers, f, indent=2)
    
    return covers

if __name__ == "__main__":
    data = scrape_covers()
    with open("covers.json", "w") as f:
        json.dump(data, f, indent=2)
