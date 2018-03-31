import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
height, width, ch = image.shape
cv2.imshow('Original', image)

blur = cv2.GaussianBlur(image, (55, 5), 0)
cv2.imshow('Gaussian Blur', blur)

kernel = np.ones((5, 5), 'uint8')

er = cv2.erode(image, kernel, iterations=1)
di = cv2.dilate(image, kernel, iterations=1)

cv2.imshow('Erosion', er)
cv2.moveWindow('Erosion', 0, height)
cv2.imshow('Dilation', di)

cv2.waitKey(0)
cv2.destroyAllWindows()
