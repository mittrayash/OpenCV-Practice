import numpy as np
import cv2

img = cv2.imread('butterfly.jpg')
cv2.imshow("Butterfly", img)
cv2.moveWindow("Butterfly", 0, 0)

height, width, channels = img.shape

b, g, r = cv2.split(img)
rgb_split = np.concatenate([b, g, r], axis=1)
cv2.imshow('rgb', rgb_split)
cv2.moveWindow('rgb', 0, 0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate([h, s, v], axis=1)
cv2.imshow('hsv', hsv_split)
cv2.moveWindow('hsv', 0, height)

cv2.waitKey(0)
cv2.destroyAllWindows()