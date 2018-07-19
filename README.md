# WIP Dashboard for Suzuki GS 500 F -04
This project could be used for any motorcycle.

## Requirements
- Gear indicator
- Temperature display ✓
- Current time display ✓
- Dashcam
- GPS Tracking and logging
- Trip counter and logging
   * Estimated mileage left

## Hardware
- Raspberry Pi 3 ✓
- Power source ✓
    * I'm using a phone holders USB-port. Outputs 5V 2.1A which should be perfect for the Pi3.
- BMP280 Temperature Sensor ✓
    * Using [RPi Spy's BME280 script for temperature reading](https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py). This works for BMP280 too. Script included in this repo.
- USB Webcam OR RPi Camera ✓
- 0.96" SPI OLED Screen (for time and temperature) ✓
    * Required: [Adafruit Python SSD1306 Library](https://github.com/adafruit/Adafruit_Python_SSD1306)
- External drive for saving dashcam footage. ✓
    * e.g. 64GB thumbdrive
- GPS Chip/usb
- Magnetic Reed switches for gear indicator ✓
- Magnet
- 7-segment display 
- Enclosure
    * 3D-print ?
    
