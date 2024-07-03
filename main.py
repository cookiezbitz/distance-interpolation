import numpy

import cv2
import matplotlib.pyplot as plt

import os

alive = True
win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while alive:
    ret, frame = source.read()
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        alive = False
        break
    elif key == ord('s'):
        cv2.imwrite('screenshot.png', frame)
    elif key == ord('f'):
        cv2.imwrite('filtered.png', result)


source.release()
cv2.destroyWindow(win_name)