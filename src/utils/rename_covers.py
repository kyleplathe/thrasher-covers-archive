import os
import shutil
from datetime import datetime
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
RESIZED_COVERS_DIR = PROJECT_ROOT / "images" / "resized"
BACKUP_DIR = PROJECT_ROOT / "images" / "resized_backup"

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

def rename_covers():
    duplicates = []
    
    # Create backup directory if it doesn't exist
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get all jpg files from resized_covers directory
    for filename in os.listdir(RESIZED_COVERS_DIR):
        if filename.endswith('.jpg'):
            date = extract_date_from_filename(filename)
            if date:
                year, month = date.split('-')
                new_filename = f"lock_screen_{month}{year}.jpg"
                old_path = RESIZED_COVERS_DIR / filename
                new_path = RESIZED_COVERS_DIR / new_filename
                
                # Check for duplicates
                if new_path.exists():
                    duplicates.append((filename, new_filename))
                    continue
                
                # Backup original file
                backup_path = BACKUP_DIR / filename
                shutil.copy2(old_path, backup_path)
                
                # Rename file
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
    
    if duplicates:
        print("\nDuplicate files found (not renamed):")
        for old, new in duplicates:
            print(f"  {old} -> {new}")

if __name__ == '__main__':
    rename_covers() 