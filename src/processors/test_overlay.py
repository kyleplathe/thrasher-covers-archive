from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
OVERLAYS_DIR = PROJECT_ROOT / "images" / "overlays"
RESIZED_COVERS_DIR = PROJECT_ROOT / "images" / "resized" / "resized_covers"
OUTPUT_DIR = PROJECT_ROOT / "images" / "combined"

def create_test_overlay():
    """Create a test metadata overlay with example data."""
    # Create a transparent overlay
    width = 1080  # Match the width of resized covers
    height = 200  # Larger height for the metadata overlay
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
    
    # Example metadata for April 1984
    month = "April"
    year = "1984"
    skater = "Bryce Kanights"
    trick = "Frontside Air"
    spot = ""
    location = "Berkeley, CA"
    
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
    spot_location = f"{spot} {location}"
    spot_location_width = draw.textlength(spot_location, font=small_font)
    draw.text(((width - spot_location_width) // 2, 100), spot_location, fill=(255, 255, 255, 255), font=small_font)
    
    # Save the overlay
    OVERLAYS_DIR.mkdir(parents=True, exist_ok=True)
    overlay_path = OVERLAYS_DIR / "test_overlay.png"
    overlay.save(overlay_path, 'PNG')
    
    # Combine with the April 1984 cover
    try:
        cover_path = RESIZED_COVERS_DIR / "lock_screen_041984.jpg"
        if cover_path.exists():
            # Open the cover image
            cover = Image.open(cover_path).convert('RGBA')
            
            # Calculate the position to place the overlay
            # Position it higher on the cover
            overlay_x = (cover.width - overlay.width) // 2
            overlay_y = cover.height - overlay.height - 150  # 150px padding from bottom
            
            # Create a new image with the same size as the cover
            combined = Image.new('RGBA', cover.size)
            
            # Paste the cover image
            combined.paste(cover, (0, 0))
            
            # Paste the overlay
            combined.paste(overlay, (overlay_x, overlay_y), overlay)
            
            # Save the combined image
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output_path = OUTPUT_DIR / "test_combined.png"
            combined.save(output_path, 'PNG')
            print(f"Created test combined image at: {output_path}")
        else:
            print(f"Cover image not found: {cover_path}")
    except Exception as e:
        print(f"Error combining images: {e}")

if __name__ == '__main__':
    create_test_overlay() 