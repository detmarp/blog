#!/usr/bin/env python
# https://python-pillow.org/
# http://effbot.org/imagingbook/pil-index.htm

from __future__ import division # for proper "3" division behavior
import random
import PIL as pillow
from PIL import Image
from PIL import ImageFont, ImageDraw

# basics

little_red_square = Image.new("RGB", (64, 64), "red")
little_red_square.save("_temp_pillow_little_red_square.png")

copy = Image.open("_temp_pillow_little_red_square.png")
copy.save("_temp_pillow_copy.png")

# text
text = Image.new("RGB", (256, 64), "#a0b0c0")
draw = ImageDraw.Draw(text) # create a 'draw' object that can draw into the 'text' image
font = ImageFont.load_default()
draw.text((10, 10), "hello", font=font, fill="black")
text.save("_temp_pillow_text.jpg")

# lines
graph = Image.new("RGB", (256, 256), "#e0e0e0")
draw = ImageDraw.Draw(graph)
color = "#0000a0"
for i in range(0, 257, 16):
    x = i if i < 256 else 255
    draw.line([0, x, 255, x], fill=color)
    draw.line([x, 0, x, 255], fill=color)
graph.save("_temp_pillow_graph.png")


def lerp(t, a, b):
    return a + (b - a) * t

def lerp_color(t, a, b):
    return (
        int(lerp(t, a[0], b[0])),
        int(lerp(t, a[1], b[1])),
        int(lerp(t, a[2], b[2])))

def diagonal_gradient(image, color1, color2):
    width, height = image.size
    for y in range (0, height):
        for x in range (0, width):
            t = (x + y) / (width + height)
            color = lerp_color(t, color1, color2)
            image.putpixel((x, y), color)

# cut and paste
# ... make some source squares
red = Image.new("RGB", (32, 32))
diagonal_gradient(red, (255, 0, 0), (255, 128, 0))
orange = Image.new("RGB", (32, 32))
diagonal_gradient(orange, (255, 128, 0), (255, 255, 0))
yellow = Image.new("RGB", (32, 32))
diagonal_gradient(yellow, (255, 255, 0), (128, 255, 0))

# ... fill new image with rotated squares
quilt = Image.new("RGB", (256, 256))
for y in range(0, 255, 32):
    for x in range(0, 255, 32):
        to = (x, y, x + 32, y + 32)
        angle = random.randrange(3) * 90
        copy = random.choice([red, orange, yellow]).copy().rotate(angle)
        quilt.paste(copy, to)

quilt.save("_temp_pillow_quilt.png")
