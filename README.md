# Thrasher Cover Daily

This project scrapes all Thrasher magazine covers, resizes them to fit iPhone lock screens, and uses a JSON file to automate a daily update via a shortcut.

## Overview

- **Scraping**: A script is used to scrape all Thrasher magazine covers.
- **Resizing**: The covers are resized to fit iPhone lock screens.
- **Automation**: A JSON file is used to build a shortcut that automatically updates the lock screen daily.

## Key Information for Developers

- The resized covers are stored in the `resized_covers` directory.
- The `resized_covers_index.json` file contains metadata for all resized covers, including filenames, URLs, and dates.
- The raw URL format for accessing the resized covers is:
  ```
  https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers/lock_screen_[Month][Year].jpg
  ```
- A link to the shortcut will be provided soon.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Run the scripts to scrape and resize the covers.
4. Use the JSON file to build your shortcut for daily updates.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License.

## Latest Thrasher Cover

![Latest Thrasher Cover](https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers/lock_screen_11202024.jpg)

**Year:** 2024  
**Month:** November 