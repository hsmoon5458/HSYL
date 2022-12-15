import cv2

# read the image
image = cv2.imread('sailing.jpg')

# flip the image
# 1 indicates a horizontal flip
flip = cv2.flip(image, 1)

# present the original and flippe images respectively
cv2.imshow('original', image)
cv2.imshow('flipped', flip)

# images presented on the screen until a user closes them out
cv2.waitKey(0)