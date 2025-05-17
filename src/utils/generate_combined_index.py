import os
import json
from pathlib import Path

# Set up paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
COMBINED_DIR = PROJECT_ROOT / "images" / "combined"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Base URL for GitHub raw access (update with your username/repo if needed)
BASE_URL = "https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/combined"

index = []
for filename in sorted(os.listdir(COMBINED_DIR)):
    if filename.endswith(".png"):
        index.append({
            "filename": filename,
            "url": f"{BASE_URL}/{filename}"
        })

with open(OUTPUT_DIR / "combined_covers_index.json", "w") as f:
    json.dump(index, f, indent=2)

print(f"Generated {OUTPUT_DIR / 'combined_covers_index.json'} with {len(index)} entries.") 