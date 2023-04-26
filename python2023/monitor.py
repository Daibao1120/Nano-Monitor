# -*- coding: utf-8 -*-
import Adafruit_SSD1306

import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import cv2
import socket

#OLED初始化
OLED = Adafruit_SSD1306.SSD1306_128_32(rst = None, i2c_bus = 0, gpio = 1)
OLED.begin()
OLED.clear()
OLED.display()
time.sleep(1)

#外觀
font = ImageFont.truetype('華康娃娃體.TTF', size = 14)
width = OLED.width
height = OLED.height
image = Image.new("1", (width,height))

#GetIP
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#

while True:

	#現在時間
    	localtime = time.localtime()
    	timeresult = time.strftime("%Y-%m-%d \n %I:%M:%S %p", localtime)
    	
    	#oled顯示
    	Draw = ImageDraw.Draw(image)
    	Draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    	Draw.text((0, 0), timeresult, font=font ,fill=255)
    	OLED.image(image)
    	OLED.display()
    	time.sleep(1)
