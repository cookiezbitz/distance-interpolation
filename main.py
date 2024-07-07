import numpy

import cv2
import matplotlib.pyplot as plt

from time import sleep
import imutils
from imutils.video import VideoStream

import os
import sys
"""SETTINGS AND VARIABLES ________________________________________________________________"""

RASPBERRY_BOOL = False
# If this is run on a linux system, a picamera will be used.
# If you are using a linux system, with a webcam instead of a raspberry pi delete the following if-statement
if sys.platform == "linux":
    import picamera
    from picamera2 import Picamera2, Preview
    from picamera.array import PiRGBArray
    RASPBERRY_BOOL = True



alive = True
win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None
#merge editor

vs = VideoStream(src= 0 ,
                 usePiCamera= RASPBERRY_BOOL,
                 resolution=video_resolution,
                 framerate = 13,
                 meter_mode = "backlit",
                 exposure_mode ="auto",
                 shutter_speed = 8900,
                 exposure_compensation = 2,
                 rotation = 0).start()
sleep(0.2)


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