import numpy as np
import cv2

color = cv2.imread('butterfly.png')

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.png', gray)

b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b, g, r, b))
cv2.imwrite('rgba', rgba)
