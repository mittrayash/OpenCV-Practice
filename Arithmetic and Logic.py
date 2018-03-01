__author__ = 'mittr'

import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]


#cv2.imshow('svm', img1)
#cv2.imshow('mpl', img2)




cv2.imshow('add', img1 + img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


