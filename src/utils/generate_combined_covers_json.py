import json
from pathlib import Path
from datetime import datetime
import re

# Define paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
RESIZED_DIR = PROJECT_ROOT / "images" / "resized" / "resized_covers"
COMBINED_DIR = PROJECT_ROOT / "images" / "combined"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "all_covers.json"

def get_date_from_filename(filename):
    """Extract date from filename."""
    if filename.startswith('lock_screen_'):
        match = re.search(r'lock_screen_(\d{2})(\d{4})\.jpg', filename)
        if match:
            return f"{match.group(2)}-{match.group(1)}"
    elif filename.startswith('combined_'):
        match = re.search(r'combined_(\d{2})(\d{4})\.png', filename)
        if match:
            return f"{match.group(2)}-{match.group(1)}"
    return None

def generate_covers_list():
    """Generate a list of covers, preferring formatted versions when available."""
    covers = {}
    
    # First add all resized covers
    for file in sorted(RESIZED_DIR.glob("lock_screen_*.jpg")):
        date = get_date_from_filename(file.name)
        if not date:
            continue
            
        covers[date] = {
            "filename": file.name,
            "date": date,
            "url": f"https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/resized/resized_covers/{file.name}"
        }
    
    # Then update with combined versions where available
    for file in sorted(COMBINED_DIR.glob("combined_*.png")):
        date = get_date_from_filename(file.name)
        if date and date in covers:
            covers[date].update({
                "filename": file.name,
                "url": f"https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/combined/{file.name}"
            })
    
    # Convert to list and sort by date
    covers_list = list(covers.values())
    
    # Create the final list
    archive = {
        "generated_at": datetime.now().isoformat(),
        "total_covers": len(covers_list),
        "covers": covers_list
    }
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(archive, f, indent=2)
    
    print(f"Generated list with {len(covers_list)} covers")
    print(f"Output file: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_covers_list() 