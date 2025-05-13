import json
import os
from datetime import datetime
from urllib.parse import quote

def extract_date_from_filename(filename):
    # Remove the lock_screen_ prefix and .jpg extension
    name = filename.replace('lock_screen_', '').replace('.jpg', '')
    
    # Handle new format (e.g., 25_05_Jamie_Foy...)
    if '_' in name:
        parts = name.split('_')
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            year = '20' + parts[0]  # Convert 25 to 2025
            month = parts[1]
            return f"{year}-{month.zfill(2)}"
    
    # Handle format with year in filename (e.g., 2024_12_Thrasher...)
    if name.startswith('2024_'):
        parts = name.split('_')
        if len(parts) >= 2:
            year = parts[0]
            month = parts[1]
            return f"{year}-{month.zfill(2)}"
    
    # Handle format with year and month (e.g., January2024)
    months = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    
    for month, num in months.items():
        if name.startswith(month):
            year = name[len(month):]
            if year.isdigit():
                return f"{year}-{num}"
    
    # Handle format with year and month (e.g., January_2023_Cover)
    for month, num in months.items():
        if name.startswith(month + '_'):
            parts = name.split('_')
            if len(parts) >= 2 and parts[1].isdigit():
                year = parts[1]
                return f"{year}-{num}"
    
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