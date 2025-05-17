from PIL import Image, ImageDraw, ImageFont
import json
from pathlib import Path
import logging

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
DATA_DIR = PROJECT_ROOT / "data" / "raw"
OVERLAYS_DIR = PROJECT_ROOT / "images" / "overlays"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_metadata_overlay(metadata, output_path):
    """Create a metadata overlay image with the specified information."""
    # Create a transparent overlay
    width = 1080  # Match the width of resized covers
    height = 200  # Height for the metadata overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Load font (you may need to adjust the font path)
    try:
        font = ImageFont.truetype("Arial", 36)
        small_font = ImageFont.truetype("Arial", 24)
    except IOError:
        # Fallback to default font if Arial is not available
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Extract metadata
    month = metadata.get('month', '')
    year = metadata.get('year', '')
    skater = metadata.get('skater', '')
    trick = metadata.get('trick', '')
    spot = metadata.get('spot', '')
    location = metadata.get('location', '')
    
    # Draw the text
    # Title (Month Year)
    title = f"{month} {year}"
    title_width = draw.textlength(title, font=font)
    draw.text(((width - title_width) // 2, 10), title, fill=(255, 255, 255, 255), font=font)
    
    # Skater and Trick
    skater_trick = f"{skater} - {trick}"
    skater_trick_width = draw.textlength(skater_trick, font=small_font)
    draw.text(((width - skater_trick_width) // 2, 60), skater_trick, fill=(255, 255, 255, 255), font=small_font)
    
    # Spot and Location
    spot_location = f"{spot}, {location}"
    spot_location_width = draw.textlength(spot_location, font=small_font)
    draw.text(((width - spot_location_width) // 2, 100), spot_location, fill=(255, 255, 255, 255), font=small_font)
    
    # Save the overlay
    overlay.save(output_path, 'PNG')
    logging.info(f"Created metadata overlay: {output_path}")

def generate_overlays():
    """Generate metadata overlays for all covers."""
    # Create overlays directory if it doesn't exist
    OVERLAYS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load metadata from JSON file
    metadata_file = DATA_DIR / "covers.json"
    try:
        with open(metadata_file, 'r') as f:
            covers = json.load(f)
    except FileNotFoundError:
        logging.error(f"Metadata file not found: {metadata_file}")
        return
    
    # Generate overlays for each cover
    for cover in covers:
        month = cover.get('month', '')
        year = cover.get('year', '')
        if month and year:
            # Create filename for the overlay
            overlay_filename = f"overlay_{month.lower()}_{year}.png"
            output_path = OVERLAYS_DIR / overlay_filename
            
            # Create the overlay
            create_metadata_overlay(cover, output_path)

if __name__ == '__main__':
    generate_overlays() 