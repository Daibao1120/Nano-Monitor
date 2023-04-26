import requests
import Adafruit_SSD1306
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import cv2
from bs4 import BeautifulSoup

r = requests.get("")##https~~~.html

soup = BeautifulSoup(r.text, "html.parser")
sel  = soup.select("div.title a")

OLED = Adafruit_SSD1306.SSD1306_128_32(rst = None, i2c_bus = 0, gpio = 1)

OLED.begin()

OLED.clear()
OLED.display()
time.sleep(1)

font_path = os.path.join(cv2.__path__[0], 'qt', 'fonts', 'DejaVuSans.ttf')
font = ImageFont.truetype(font_path, size = 20)
width = OLED.width
height = OLED.height
image = Image.new("1", (width,height))
