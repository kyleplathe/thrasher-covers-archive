# Thrasher Cover Daily

![Full Size Jamie Foy Cover](https://www.thrashermagazine.com/images/image/Covers_Archive/25_05_Jamie_Foy_Burnett_Frontside_Half_Cab_Nosegrind_CV1TH0525_1080.jpg)

## Shortcut Link

You can use the shortcut to set a random Thrasher cover as your lock screen: [Thrasher Cover Daily Shortcut](https://www.icloud.com/shortcuts/3082f51868c54982bddab31254876771)

## Important Note About Automation

Due to Apple's security restrictions, shortcuts cannot automatically change your lock screen through the standard automation system. However, there are several ways to use this shortcut:

1. **Manual Trigger**: Tap the shortcut in the Shortcuts app or add it to your home screen
2. **Siri Command**: Say "Hey Siri, run Thrasher Cover Daily"
3. **Custom Automation**: For true automation, you'll need to build the logic directly in the Shortcuts app's Automation tab

## How to Set Up Custom Automation

To create a custom automation that can change your lock screen:

1. Open the Shortcuts app on your iPhone
2. Tap on the "Automation" tab at the bottom
3. Tap the "+" button to create a new automation
4. Choose "Time of Day" as the trigger
5. Set your preferred time
6. Add these actions in sequence:
   - "Get Contents of URL" (use: https://raw.githubusercontent.com/kyleplathe/thrasher-covers-archive/main/resized_covers_index.json)
   - "Get Dictionary from Input"
   - "Get Dictionary Value" (key: "covers")
   - "Get Item from List" (Random Item)
   - "Get Dictionary Value" (key: "url")
   - "Get Contents of URL"
   - "Set Wallpaper"
7. Toggle "Run Immediately" ON
8. Toggle "Notify When Run" OFF
9. Tap "Done" to save the automation

## About

This project automatically scrapes and resizes Thrasher magazine covers to fit iPhone lock screens. The covers are updated daily through automated processes, ensuring you always have access to the latest and classic Thrasher covers.

## License

This project is licensed under the MIT License. 
