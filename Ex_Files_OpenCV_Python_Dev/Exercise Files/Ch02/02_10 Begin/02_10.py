import numpy as np
import cv2

# Global variables
canvas = np.ones([500, 500, 3], 'uint8') * 255
color = (255, 0, 0)
line_width = -1
radius = 3
point = (0, 0)
pressed = False

# click callback
def click(event, x, y, flags, param):
    global canvas, point, pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        print("LButton Down")
        point = (x, y)
        pressed = True
        cv2.circle(canvas, point, radius, color, line_width)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        print("Mouse Move")
        point = (x, y)
        cv2.circle(canvas, point, radius, color, line_width)
    elif event == cv2.EVENT_LBUTTONUP:
        print("LButton Up")
        point = (x, y)
        pressed = False


# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

    cv2.imshow("canvas", canvas)

    # key capture every 1ms
    ch = cv2.waitKey(1)

    if ch & 0xFF == ord('g'):
        color = (0, 255, 0)
    elif ch & 0xFF == ord('b'):
        color = (255, 0, 0)

    if ch & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()