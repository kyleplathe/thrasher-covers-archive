import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
OVERLAYS_DIR = PROJECT_ROOT / "images" / "overlays"
RESIZED_COVERS_DIR = PROJECT_ROOT / "images" / "resized" / "resized_covers"
OUTPUT_DIR = PROJECT_ROOT / "images" / "combined"
DATA_DIR = PROJECT_ROOT / "data" / "raw"

def create_overlay(metadata):
    """Create a metadata overlay with the provided data."""
    # Create a transparent overlay
    width = 1080  # Match the width of resized covers
    height = 200  # Height for the metadata overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Load font
    try:
        font = ImageFont.truetype("Arial", 36)
        small_font = ImageFont.truetype("Arial", 24)
    except IOError:
        # Fallback to default font if Arial is not available
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Draw the text
    # Title (Month Year)
    title = f"{metadata['month'].title()} {metadata['year']}"
    title_width = draw.textlength(title, font=font)
    draw.text(((width - title_width) // 2, 10), title, fill=(255, 255, 255, 255), font=font)
    
    # Skater and Trick
    skater_trick = f"{metadata['skater'].title()} - {metadata['trick'].title()}"
    skater_trick_width = draw.textlength(skater_trick, font=small_font)
    draw.text(((width - skater_trick_width) // 2, 60), skater_trick, fill=(255, 255, 255, 255), font=small_font)
    
    # Spot and Location
    spot_location = f"{metadata['spot']} {metadata['location']}".strip()
    if spot_location:  # Only draw if there's content
        spot_location_width = draw.textlength(spot_location, font=small_font)
        draw.text(((width - spot_location_width) // 2, 100), spot_location, fill=(255, 255, 255, 255), font=small_font)
    
    return overlay

def combine_with_cover(cover_path, overlay, output_path):
    """Combine a cover image with its overlay."""
    try:
        # Open the cover image
        cover = Image.open(cover_path).convert('RGBA')
        
        # Calculate the position to place the overlay
        overlay_x = (cover.width - overlay.width) // 2
        overlay_y = cover.height - overlay.height - 150  # 150px padding from bottom
        
        # Create a new image with the same size as the cover
        combined = Image.new('RGBA', cover.size)
        
        # Paste the cover image
        combined.paste(cover, (0, 0))
        
        # Paste the overlay
        combined.paste(overlay, (overlay_x, overlay_y), overlay)
        
        # Save the combined image
        combined.save(output_path, 'PNG')
        logging.info(f"Created combined image: {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error combining images for {cover_path}: {e}")
        return False

def get_month_number(month_str):
    """Convert month string to number, handling special cases."""
    month_str = month_str.lower()
    if month_str == 'winter':
        return '13'  # Special case for Winter issue
    try:
        return str(list(calendar.month_name).index(month_str.title())).zfill(2)
    except ValueError:
        logging.warning(f"Unknown month format: {month_str}")
        return None

def process_covers():
    """Process all covers and generate overlays."""
    # Create necessary directories
    OVERLAYS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Read the 4ply covers data
    covers_data = []
    with open(DATA_DIR / "4ply_covers.csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            covers_data.append(row)
    
    # Process each cover
    for cover in covers_data:
        # Skip covers without a skater or trick
        if not cover['skater'] or not cover['trick']:
            continue
            
        # Format the cover filename
        month_num = get_month_number(cover['month'])
        if not month_num:
            continue
            
        cover_filename = f"lock_screen_{month_num}{cover['year']}.jpg"
        cover_path = RESIZED_COVERS_DIR / cover_filename
        
        if not cover_path.exists():
            logging.warning(f"Cover image not found: {cover_path}")
            continue
        
        # Create overlay
        overlay = create_overlay(cover)
        overlay_path = OVERLAYS_DIR / f"overlay_{month_num}{cover['year']}.png"
        overlay.save(overlay_path, 'PNG')
        
        # Combine with cover
        output_path = OUTPUT_DIR / f"combined_{month_num}{cover['year']}.png"
        combine_with_cover(cover_path, overlay, output_path)

if __name__ == '__main__':
    import calendar  # Import here to avoid circular import
    process_covers() 