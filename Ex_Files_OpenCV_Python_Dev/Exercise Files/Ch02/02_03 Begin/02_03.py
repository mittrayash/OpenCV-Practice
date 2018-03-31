import numpy as np
import cv2

zeros = np.zeros([256, 512, 1], 'uint8')
cv2.imshow('zeros', zeros)

ones = np.ones([256, 512, 3], 'uint16')
cv2.imshow('ones', ones)

white = ones.copy()
white *= 2**16 - 1
cv2.imshow('white', white)

blue = ones.copy()
blue[:, :] = (2**16 - 1, 0, 0)
cv2.imshow('blue', blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
