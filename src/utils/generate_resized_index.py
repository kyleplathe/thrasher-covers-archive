import json
import os
from datetime import datetime
from urllib.parse import quote
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
RESIZED_COVERS_DIR = PROJECT_ROOT / "images" / "resized"
DATA_DIR = PROJECT_ROOT / "data" / "processed"

def extract_date_from_filename(filename):
    # Remove the lock_screen_ prefix and .jpg extension
    name = filename.replace('lock_screen_', '').replace('.jpg', '')
    # Handle format like 011981 (MMYYYY)
    if len(name) == 6 and name[:2].isdigit() and name[2:].isdigit():
        month = name[:2]
        year = name[2:]
        return f"{year}-{month}"
    return None

def generate_index():
    base_url = "https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/resized"
    covers = []
    
    # Get all jpg files from resized_covers directory
    for filename in os.listdir(RESIZED_COVERS_DIR):
        if filename.endswith('.jpg'):
            date = extract_date_from_filename(filename)
            if date:
                covers.append({
                    'filename': filename,
                    'url': f"{base_url}/{quote(filename)}",
                    'date': date
                })
    
    # Sort by date
    covers.sort(key=lambda x: x['date'], reverse=True)
    
    # Create the index
    index = {
        'generated_at': datetime.now().isoformat(),
        'total_covers': len(covers),
        'covers': covers
    }
    
    # Create processed data directory if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save to file
    index_file = DATA_DIR / "resized_covers_index.json"
    with open(index_file, 'w') as f:
        json.dump(index, f, indent=2)
    
    print(f"Generated index with {len(covers)} covers at {index_file}")

if __name__ == '__main__':
    generate_index() 