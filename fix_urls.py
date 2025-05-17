import json
import os

def fix_urls():
    # Read the JSON file
    with open('data/processed/all_covers.json', 'r') as f:
        data = json.load(f)
    
    # Fix URLs for each cover
    for cover in data['covers']:
        filename = cover['filename']
        if filename.startswith('lock_screen_'):
            cover['url'] = f"https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/resized/resized_covers/{filename}"
        elif filename.startswith('combined_'):
            cover['url'] = f"https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/images/combined/{filename}"
    
    # Write the updated JSON file
    with open('data/processed/all_covers.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    fix_urls() 