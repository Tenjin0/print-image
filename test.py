#!/usr/bin/python
# -- coding: utf-8 --
# thaitest.py - thai thermal printing test - scruss, 2014-11-04
from PIL import Image, ImageFont, ImageOps, ImageDraw
from escpos import *

text = u'ลองตัวอักษรไทย'             # Thai for ‘Thai Alphabet’, maybe?
Epson = printer.Serial(devfile="/dev/usb/lp0")  # <<< change this !!!
# Used Thai font ‘Loma’, installed by
#   sudo apt-get install fonts-tlwg-loma
# then
#   cp /usr/share/fonts/truetype/tlwg/Loma.ttf .
# Used 36 pt Loma font
font = ImageFont.truetype("Loma.ttf", 36)
box = font.getsize(text)         # work out size of text
# make an image same width as text, but twice the height
image = Image.new("RGB", (box[0], 2 * box[1]))
draw = ImageDraw.Draw(image)
# draw the text at the left edge of the box
draw.text((0, 0), text, font=font)
image = ImageOps.invert(image)   # invert image to black on white
# Epson._convert_image(image)      # output image to printer
