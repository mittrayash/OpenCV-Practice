import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    cv2.imshow('Frame', frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

print(16 // 3)
cap.release()
cv2.destroyAllWindows()