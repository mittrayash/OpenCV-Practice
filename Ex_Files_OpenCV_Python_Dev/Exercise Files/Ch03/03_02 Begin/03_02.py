import numpy as np
import cv2

bw = cv2.imread('detect_blob.png', 0)
cv2.imshow('Original', bw)

threshold = 85

ret, thresh = cv2.threshold(bw, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold applied', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
