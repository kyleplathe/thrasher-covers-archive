# Thrasher Cover Daily

![Full Size Jamie Foy Cover](https://www.thrashermagazine.com/images/image/Covers_Archive/25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg)

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

## Shortcut Link

You can use the shortcut to set a random Thrasher cover as your lock screen: [Thrasher Cover Daily Shortcut](https://www.icloud.com/shortcuts/3082f51868c54982bddab31254876771)

## How to Set Up Automation

1. Open the Shortcuts app on your iPhone.
2. Tap on the "Automation" tab at the bottom.
3. Tap the "+" button to create a new automation.
4. Choose "Time of Day" as the trigger.
5. Set the time you want the shortcut to run daily.
6. Tap "Add Action" and search for "Run Shortcut."
7. Select the "Thrasher Cover Daily" shortcut.
8. Toggle "Run Immediately" ON.
9. Toggle "Notify When Run" OFF.
10. Tap "Done" to save the automation.

Now, your iPhone will automatically set a random Thrasher cover as your lock screen at the specified time each day!