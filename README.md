# Thrasher Covers Archive Scraper

## 🆕 Latest Cover (May 2025)

![May 2025 Thrasher Cover](https://www.thrashermagazine.com/images/image/Covers_Archive/25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg)

**Year:** 2025  
**Month:** May

---

This Python script scrapes the [Thrasher Magazine Covers Archive](https://www.thrashermagazine.com/covers/) and generates a JSON file containing the year, month, and image URL for every cover in the archive.

## Features

- **Automatic scraping** of all Thrasher magazine covers from 1981 to the present.
- **Handles different URL formats** for covers across decades.
- **Outputs a clean `covers.json`** file with the following structure for each cover:
  ```json
  {
    "year": 2025,
    "month": "May",
    "url": "https://www.thrashermagazine.com/images/image/Covers_Archive/25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg"
  }
  ```

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/kyleplathe/thrasher-covers-archive.git
   cd thrasher-covers-archive
   ```

2. Run the scraper:
   ```bash
   python3 scrape_thrasher_covers.py
   ```

3. The script will output a `covers.json` file in the same directory.

## 📱 Daily Lock Screen Automation

### Option 1: Using Shortcuts App

1. **Set up the automation:**
   - Open the Shortcuts app
   - Create a new automation
   - Choose "Time of Day" trigger
   - Add "Thrasher Daily Cover" shortcut
   - Open automation settings
   - Toggle "Run Immediately" ON
   - Toggle "Notify When Run" OFF

2. **Using GitHub Raw URLs:**
   - The resized images are stored in the `resized_covers` directory
   - Use this format for the raw URL:
     ```
     https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers/lock_screen_[filename]
     ```
   - Example for May 2025 cover:
     ```
     https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers/lock_screen_25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg
     ```

3. **Run the automation:**
   - Enable the automation
   - Test it by running it manually first
   - It will now run daily at your chosen time

### Option 2: Using the Resize Script

The resize script automatically formats covers to work perfectly on modern iPhones and Android devices:

1. Process a single cover:
   ```bash
   python3 resize_cover.py
   ```

2. Process multiple covers:
   ```bash
   python3 resize_cover.py --limit 10  # Process 10 latest covers
   python3 resize_cover.py --all       # Process all covers
   ```

The script will:
- Resize covers to 1080x2340 (9:19.5 aspect ratio)
- Center and crop to maintain image quality
- Save high-quality images ready for your lock screen
- Work across iPhone X and newer models

## Notes

- The script is designed to be robust to changes in Thrasher's cover URL patterns.
- Only the year, month, and image URL are included for each cover to keep the output clean and simple.

## License

MIT License 