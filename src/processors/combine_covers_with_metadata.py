from PIL import Image
import json
from pathlib import Path
import logging

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
RESIZED_COVERS_DIR = PROJECT_ROOT / "images" / "resized"
OVERLAYS_DIR = PROJECT_ROOT / "images" / "overlays"
OUTPUT_DIR = PROJECT_ROOT / "images" / "combined"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def combine_cover_with_overlay(cover_path, overlay_path, output_path):
    """Combine a cover image with its metadata overlay."""
    try:
        # Open the cover and overlay images
        cover = Image.open(cover_path).convert('RGBA')
        overlay = Image.open(overlay_path).convert('RGBA')
        
        # Calculate the position to place the overlay (centered horizontally, at the bottom)
        overlay_x = (cover.width - overlay.width) // 2
        overlay_y = cover.height - overlay.height - 20  # 20px padding from bottom
        
        # Create a new image with the same size as the cover
        combined = Image.new('RGBA', cover.size)
        
        # Paste the cover image
        combined.paste(cover, (0, 0))
        
        # Paste the overlay
        combined.paste(overlay, (overlay_x, overlay_y), overlay)
        
        # Save the combined image
        combined.save(output_path, 'PNG')
        logging.info(f"Created combined image: {output_path}")
        
    except Exception as e:
        logging.error(f"Error combining images: {e}")

def process_all_covers():
    """Process all covers and combine them with their metadata overlays."""
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get all cover images
    cover_files = list(RESIZED_COVERS_DIR.glob('*.jpg'))
    
    for cover_path in cover_files:
        # Extract month and year from filename
        filename = cover_path.stem
        if filename.startswith('lock_screen_'):
            date_part = filename[12:]  # Remove 'lock_screen_' prefix
            if len(date_part) >= 6:  # Ensure we have at least MMYYYY
                month = date_part[:2]
                year = date_part[2:]
                
                # Construct overlay filename
                overlay_filename = f"overlay_{month}_{year}.png"
                overlay_path = OVERLAYS_DIR / overlay_filename
                
                if overlay_path.exists():
                    # Create output filename
                    output_filename = f"combined_{month}{year}.png"
                    output_path = OUTPUT_DIR / output_filename
                    
                    # Combine the images
                    combine_cover_with_overlay(cover_path, overlay_path, output_path)
                else:
                    logging.warning(f"No overlay found for {filename}")

if __name__ == '__main__':
    process_all_covers() 