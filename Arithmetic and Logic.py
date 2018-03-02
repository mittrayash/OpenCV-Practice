__author__ = 'mittr'

import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]
grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(grey, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)


dst = cv2.bitwise_or(img2_fg, img1_bg)

img1[:rows, :cols] = dst
cv2.imshow('Final Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


