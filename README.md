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

## Notes

- The script is designed to be robust to changes in Thrasher's cover URL patterns.
- Only the year, month, and image URL are included for each cover to keep the output clean and simple.

## License

MIT License 