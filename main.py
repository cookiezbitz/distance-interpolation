"""SETTINGS AND VARIABLES ________________________________________________________________"""

import numpy
import cv2
import matplotlib.pyplot as plt
from time import sleep
import os
import sys




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
        #takes a snapshot
    elif key == ord('f'):
        cv2.imwrite('filtered.png', result)
        #takes a snapshot and saves it as filtered.png, this one is for modifications


source.release()
cv2.destroyWindow(win_name)