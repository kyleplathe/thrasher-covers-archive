import json
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_metadata():
    """Load metadata from covers_with_metadata.json"""
    try:
        with open('covers_with_metadata.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("covers_with_metadata.json not found")
        return {}

def format_metadata_for_shortcuts(metadata):
    """Format metadata for iOS Shortcuts"""
    shortcuts_data = {}
    
    for cover in metadata:
        # Create filename from month and year
        month_num = datetime.strptime(cover['month'], '%B').month
        filename = f"lock_screen_{month_num:02d}{cover['year']}.jpg"
        
        # Format date for display
        formatted_date = f"{cover['month']} {cover['year']}"
        
        # Create metadata text
        metadata_text = f"{formatted_date}\n"
        
        if cover.get('skater'):
            metadata_text += f"Skater: {cover['skater']}\n"
        if cover.get('trick'):
            metadata_text += f"Trick: {cover['trick']}\n"
        if cover.get('spot'):
            metadata_text += f"Spot: {cover['spot']}"
        elif cover.get('location'):
            metadata_text += f"Location: {cover['location']}"
        
        # Add to shortcuts data
        shortcuts_data[filename] = {
            'text': metadata_text,
            'position': 'bottom',  # iOS Shortcuts position
            'font_size': 24,       # Adjust as needed
            'font_color': 'white', # Adjust as needed
            'background_color': 'black', # Adjust as needed
            'background_opacity': 0.7    # Adjust as needed
        }
    
    return shortcuts_data

def main():
    # Load metadata
    metadata = load_metadata()
    
    # Format for shortcuts
    shortcuts_data = format_metadata_for_shortcuts(metadata)
    
    # Save to JSON file
    output_file = 'shortcuts_metadata.json'
    with open(output_file, 'w') as f:
        json.dump(shortcuts_data, f, indent=2)
    
    logger.info(f"Generated {output_file} with metadata for {len(shortcuts_data)} covers")

if __name__ == "__main__":
    main() 