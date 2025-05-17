import os
import json
from pathlib import Path
import re

# Set up paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
RESIZED_INDEX_PATH = PROJECT_ROOT / "data" / "raw" / "resized_covers_index.json"
COVERS_JSON_PATH = PROJECT_ROOT / "data" / "raw" / "covers.json"
COMBINED_DIR = PROJECT_ROOT / "images" / "combined"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Base URL for combined images
BASE_URL_COMBINED = "https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/combined"

# Helper to extract skater, trick, photographer from 2025 cover URLs
COVER_2025_PATTERN = re.compile(r"25_\d{2}_(.+?)_(.+?)_(.+?)_CV1TH\d{4}")

def extract_2025_meta(url):
    # Example: 25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg
    m = COVER_2025_PATTERN.search(url)
    if m:
        skater = m.group(1).replace('_', ' ')
        photographer = m.group(2).replace('_', ' ')
        trick = m.group(3).replace('_', ' ')
        return skater, trick, photographer
    return None, None, None

# Load the resized covers index
with open(RESIZED_INDEX_PATH, 'r') as f:
    resized_index = json.load(f)
resized_entries = resized_index.get('covers', [])
resized_filenames = {entry['filename'] for entry in resized_entries}
master_list = resized_entries.copy()

# Load covers.json for 2025 meta
with open(COVERS_JSON_PATH, 'r') as f:
    covers_json = json.load(f)

# Build a lookup for 2025 covers by (year, month)
covers_2025 = {(c['year'], c['month']): c for c in covers_json if c['year'] == 2025}

# Update master_list with 2025 meta if available
for entry in master_list:
    # Only update 2025 covers
    if entry.get('date', '').startswith('2025-'):
        # Get month as full name
        month_num = entry['date'].split('-')[1]
        import calendar
        month_name = calendar.month_name[int(month_num)]
        meta = covers_2025.get((2025, month_name))
        if meta:
            skater, trick, photographer = extract_2025_meta(meta['url'])
            if skater:
                entry['skater'] = skater
            if trick:
                entry['trick'] = trick
            if photographer:
                entry['photographer'] = photographer

# Add missing covers from combined images
for filename in sorted(os.listdir(COMBINED_DIR)):
    if filename.endswith('.png'):
        if filename not in resized_filenames:
            master_list.append({
                "filename": filename,
                "url": f"{BASE_URL_COMBINED}/{filename}"
            })

# Write the master archive
with open(OUTPUT_DIR / "master_covers_archive.json", "w") as f:
    json.dump(master_list, f, indent=2)

print(f"Generated {OUTPUT_DIR / 'master_covers_archive.json'} with {len(master_list)} entries.") 