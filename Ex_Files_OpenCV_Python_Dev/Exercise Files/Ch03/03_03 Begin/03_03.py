import numpy as np
import cv2

original = cv2.imread('sudoku.png', 0)
cv2.imshow('Original', original)

_, thresh_binary = cv2.threshold(original, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold', thresh_binary)

# Note that the block size (301 here) must be an odd number!!!
thresh_adaptive = cv2.adaptiveThreshold(original, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 301, 1)


cv2.imshow('Adaptive Threshold', thresh_adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
