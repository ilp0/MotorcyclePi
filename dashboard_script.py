import bmp280
import datetime
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()
current_display = 0
dataview = ""
while True:
    
    if current_display == 0:
        
        # Read temperature from bmp280
        temperature, pressure, humidity = bmp280.readBME280All()
        # Get current time
        dataview = str(temperature) + " C"

    if current_display == 1:
        now = datetime.datetime.now()
        dataview = "%02s:%02s" % (now.hour, now.minute)
   
    # Clear
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Draw temperature and time text.
    draw.text((x, top), dataview, font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    if current_display == 0:
        current_display = 1
    else:
        current_display = 0
    time.sleep(5)
