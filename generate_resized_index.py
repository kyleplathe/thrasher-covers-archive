import json
import os
from datetime import datetime
from urllib.parse import quote

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
    base_url = "https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers"
    covers = []
    
    # Get all jpg files from resized_covers directory
    for filename in os.listdir('resized_covers'):
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
    
    # Save to file
    with open('resized_covers_index.json', 'w') as f:
        json.dump(index, f, indent=2)
    
    print(f"Generated index with {len(covers)} covers")

if __name__ == '__main__':
    generate_index() 