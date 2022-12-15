import numpy as np
import cv2
from PIL import Image

def flip(x):

    image = Image.open(x) 
    height = image.get_height()
    width = image.get_width()
    new_image = Image(height, width)

    for r in range(height):
        for c in range(width):
            temp = image.get_pixel(r, c)
            temp2 = new_image.get_pixel(r, c)
            new_image.set_pixel((height-1)-r,(width-1)-c,temp)

new = flip('sailing.jpg')
cv2.imshow('new', new)