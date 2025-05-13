import requests
from PIL import Image
import io
import json
import os
import argparse

# Universal size that works well across modern iPhones
# Using 9:19.5 aspect ratio which works well for iPhone X and newer
TARGET_WIDTH = 1080
TARGET_HEIGHT = 2340

def download_and_resize_cover(url, output_dir="resized_covers"):
    """Download a cover image and resize it for iPhone lock screen."""
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # Download the image
        response = requests.get(url)
        response.raise_for_status()
        
        # Open the image
        img = Image.open(io.BytesIO(response.content))
        
        # Calculate aspect ratios
        target_ratio = TARGET_HEIGHT / TARGET_WIDTH
        img_ratio = img.height / img.width
        
        if img_ratio > target_ratio:
            # Image is too tall, crop width
            new_width = int(img.height / target_ratio)
            left = (img.width - new_width) // 2
            img = img.crop((left, 0, left + new_width, img.height))
        else:
            # Image is too wide, crop height
            new_height = int(img.width * target_ratio)
            top = (img.height - new_height) // 2
            img = img.crop((0, top, img.width, top + new_height))
        
        # Resize to target dimensions
        img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
        
        # Save the resized image
        filename = url.split('/')[-1]
        output_path = os.path.join(output_dir, f"lock_screen_{filename}")
        img.save(output_path, quality=95)
        
        print(f"✅ Resized cover saved to: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return None

def process_covers(covers, limit=None):
    """Process multiple covers."""
    if limit:
        covers = covers[:limit]
    
    successful = 0
    for cover in covers:
        print(f"\n🖼️ Processing: {cover['month']} {cover['year']}")
        if download_and_resize_cover(cover['url']):
            successful += 1
    
    print(f"\n✨ Successfully processed {successful} out of {len(covers)} covers")

def main():
    parser = argparse.ArgumentParser(description='Resize Thrasher covers for iPhone lock screens')
    parser.add_argument('--limit', type=int, help='Number of covers to process (default: latest only)')
    parser.add_argument('--all', action='store_true', help='Process all covers')
    args = parser.parse_args()

    # Read the covers.json file
    try:
        with open('covers.json', 'r') as f:
            covers = json.load(f)
    except FileNotFoundError:
        print("❌ covers.json not found. Please run scrape_thrasher_covers.py first.")
        return
    
    if args.all:
        print("📱 Processing all covers...")
        process_covers(covers)
    elif args.limit:
        print(f"📱 Processing {args.limit} latest covers...")
        process_covers(covers, args.limit)
    else:
        # Get the latest cover
        latest_cover = covers[0]
        print(f"🖼️ Processing latest cover: {latest_cover['month']} {latest_cover['year']}")
        output_path = download_and_resize_cover(latest_cover['url'])
        
        if output_path:
            print("\n📱 How to use the resized cover:")
            print("1. Transfer the image to your iPhone")
            print("2. Open Photos app")
            print("3. Select the image")
            print("4. Tap Share > Use as Wallpaper")
            print("5. Adjust position if needed")
            print("6. Tap Set > Set Lock Screen")

if __name__ == "__main__":
    main() 