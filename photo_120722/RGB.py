import cv2

# read the image
image = cv2.imread('mosaic.jpg')

# copy the image, then remove blue and green from the image
# first : represents the entire rows
# second : represents the entire columns
# 0 indicates blue, 1 indicates green, and 2 indicates red color
red = image.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0

# copy the image, then remove blue and red from the image
green = image.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

# copy the image, then remove green and red from the image
blue = image.copy()
blue[:, :, 1] = 0
blue[:, :, 2] = 0

# present the original, red, green, and blue images respectively
cv2.imshow('original', image)
cv2.imshow('RED', red)
cv2.imshow('GREEN', green)
cv2.imshow('BLUE', blue)

# images presented on the screen until a user closes them out
cv2.waitKey(0)