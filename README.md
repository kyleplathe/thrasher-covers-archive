# Thrasher Covers Archive

A project to archive and process Thrasher Magazine cover images.

## Overview

- **Latest Cover Image:** The latest Thrasher cover image is displayed at the top of the project page.
- **iOS Shortcut:** Use the Thrasher Cover Daily shortcut to automatically set a random Thrasher cover as your iPhone lock screen.
- **Shortcut Link:** [Thrasher Cover Daily Shortcut](https://www.icloud.com/shortcuts/3082f51868c54982bddab31254876771)

## Quick Update on How to Use the Shortcut

Due to Apple's security restrictions, we can't automatically change lock screens through standard automation. But don't worry, here's how to make it work:

📱 **THREE WAYS TO USE IT:**
1️⃣ Tap the shortcut in the Shortcuts app
2️⃣ Say "Hey Siri, run Thrasher Cover Daily"
3️⃣ Set up a custom automation (instructions below)

⚡️ **CUSTOM AUTOMATION SETUP:**
1. Open Shortcuts app
2. Go to Automation tab
3. Create new automation
4. Choose "Time of Day"
5. Set your preferred time
6. Add these actions in order:
   • Get Contents of URL (use the JSON link)
   • Get Dictionary from Input
   • Get Dictionary Value (key: "covers")
   • Get Random Item from List
   • Get Dictionary Value (key: "url")
   • Get Contents of URL
   • Set Wallpaper

## Project Structure

```
thrasher-covers-archive/
├── src/                    # Source code directory
│   ├── scrapers/          # Scraping scripts
│   │   ├── scrape_thrasher_covers.py
│   │   └── scrape_4ply_metadata.py
│   ├── processors/        # Image processing scripts
│   │   ├── resize_cover.py
│   │   ├── combine_covers_with_metadata.py
│   │   ├── generate_metadata_overlay.py
│   │   └── generate_metadata_json.py
│   └── utils/             # Utility scripts
│       ├── generate_resized_index.py
│       └── rename_covers.py
├── data/                  # Data directory
│   ├── raw/              # Raw data (JSON, CSV)
│   └── processed/        # Processed data
├── images/               # Image directories
│   ├── original/        # Original cover images
│   ├── resized/         # Resized cover images
│   └── overlays/        # Metadata overlays
├── tests/               # Test files and samples
└── docs/               # Documentation
```

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Scrape cover images:
```bash
python src/scrapers/scrape_thrasher_covers.py
```

2. Resize images:
```bash
python src/processors/resize_cover.py
```

3. Generate metadata:
```bash
python src/processors/generate_metadata_json.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 