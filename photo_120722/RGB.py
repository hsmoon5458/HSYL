import cv2

image = cv2.imread('mosaic.jpg')

red = image.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0

green = image.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = image.copy()
blue[:, :, 1] = 0
blue[:, :, 2] = 0

cv2.imshow('original', image)
cv2.imshow('RED', red)
cv2.imshow('GREEN', green)
cv2.imshow('BLUE', blue)

cv2.waitKey(0)