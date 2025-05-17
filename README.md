# Thrasher Covers Archive

This project archives Thrasher Magazine covers and provides a master JSON file for automation.

## Overview

- **Master Archive:** The master archive (`data/processed/master_covers_archive.json`) contains all available covers, including 2025 covers with metadata (skater, trick, photographer) extracted from the cover URLs.
- **4ply Website:** For additional resources and historical data, visit [4ply](https://4plymagazine.com/).
- **Automation:** Use the master archive JSON for your iOS Shortcut automation. The JSON link is:
  ```
  https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/data/processed/master_covers_archive.json
  ```
- **Shortcut Automation Logic:** Screenshots of the shortcut automation logic will be added for better reference.

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

1. Clone the repository.
2. Use the master archive JSON for automation.
3. Refer to the 4ply website for additional resources.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 