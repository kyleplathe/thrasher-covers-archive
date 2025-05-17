import csv
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

COVERS_CSV = "4ply_covers.csv"
COVERS_JSON = "covers.json"
OUTPUT_JSON = "covers_with_metadata.json"

MONTHS = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

def normalize_month(month):
    month = month.strip().lower()
    if month in MONTHS:
        return month.capitalize()
    # Try to parse as a number (e.g., 1, 01)
    try:
        idx = int(month)
        if 1 <= idx <= 12:
            return MONTHS[idx - 1].capitalize()
    except Exception:
        pass
    return month.capitalize()

def load_4ply_metadata():
    metadata = []
    with open(COVERS_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Normalize month and year
            row_month = normalize_month(row['month'])
            row_year = int(row['year']) if row['year'].isdigit() else None
            row['month'] = row_month
            row['year'] = row_year
            metadata.append(row)
    return metadata

def merge_metadata():
    logger.info("Merging 4plymag.com metadata with covers.json...")
    try:
        with open(COVERS_JSON, "r") as f:
            covers = json.load(f)
    except FileNotFoundError:
        logger.error(f"❌ {COVERS_JSON} not found. Please run scrape_thrasher_covers.py first.")
        return

    metadata = load_4ply_metadata()
    matches = 0
    for cover in covers:
        cover_month = cover["month"].strip().capitalize()
        cover_year = int(cover["year"])
        # Find matching metadata row
        for row in metadata:
            if row["month"] == cover_month and row["year"] == cover_year:
                # Merge fields
                cover.update({
                    "skater": row.get("skater", ""),
                    "trick": row.get("trick", ""),
                    "obstacle": row.get("obstacle", ""),
                    "detailer": row.get("detailer", ""),
                    "staircount": row.get("staircount", ""),
                    "spot": row.get("spot", ""),
                    "location": row.get("location", ""),
                    "notes": row.get("notes", ""),
                    "special": row.get("special", ""),
                    "soty": row.get("soty", "")
                })
                matches += 1
                break
    logger.info(f"Matched and merged metadata for {matches} covers.")
    with open(OUTPUT_JSON, "w") as f:
        json.dump(covers, f, indent=2)
    logger.info(f"Saved merged data to {OUTPUT_JSON}.")

if __name__ == "__main__":
    merge_metadata() 