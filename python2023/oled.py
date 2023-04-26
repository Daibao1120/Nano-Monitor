# -*- coding: utf-8 -*-
import Adafruit_SSD1306

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import cv2
import socket

OLED = Adafruit_SSD1306.SSD1306_128_32(rst = None, i2c_bus = 0, gpio = 1)

OLED.begin()

OLED.clear()
OLED.display()
time.sleep(1)

font_path = os.path.join(cv2.__path__[0], 'qt', 'fonts', '華康娃娃體.TTF')
font = ImageFont.truetype('華康娃娃體.TTF', size = 30)

width = OLED.width
height = OLED.height
image = Image.new("1", (width,height))

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

im = Image.open("sc.png")

while True:
	Draw = ImageDraw.Draw(image)
	Draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
	Draw.text((0, 0), "幹，好睏", font=font ,fill=255)
	
	OLED.image(image)
	OLED.display()
	time.sleep(1)
