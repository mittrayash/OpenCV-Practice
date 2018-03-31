import numpy as np
import cv2

img = cv2.imread('faces.jpeg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

complete = np.concatenate((h, s, v), axis=1)
complete = cv2.resize(complete, (0, 0), fx=0.15, fy=0.15)
h = cv2.resize(h, (0, 0), fx=0.15, fy=0.15)
s = cv2.resize(s, (0, 0), fx=0.15, fy=0.15)
cv2.imshow("Hue, Saturation, Value", complete)

_, thresh1 = cv2.threshold(h, 10, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('hue', thresh1)
cv2.moveWindow('hue', 100, 100)
_, thresh2 = cv2.threshold(s, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('sat', thresh2)

thresh = cv2.bitwise_and(thresh1, thresh2)
cv2.imshow('final', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
