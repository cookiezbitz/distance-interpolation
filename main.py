"""SETTINGS AND VARIABLES ________________________________________________________________"""

## This is intended to work on linux systems
import numpy
import cv2
import matplotlib.pyplot as plt
from time import sleep
import os
import sys
from picamera2 import Picamera2, Preview

# Defining Variables
alive = True
win_name1 = "Right Camera"
win_name2 = "Left Camera"

# Initialize cameras
cam1 = Picamera2(0)
cam2 = Picamera2(1)
preview_config = cam1.create_preview_configuration()
preview_config2 = cam2.create_preview_configuration()
cam1.configure(preview_config)
cam2.configure(preview_config2)
cam1.start()
cam2.start()


cv2.namedWindow(win_name1, cv2.WINDOW_NORMAL)
cv2.namedWindow(win_name2, cv2.WINDOW_NORMAL)

while alive:
    # Capture an image with picamera2
    frame = cam1.capture_array()
    frame2 = cam2.capture_array()
    # Convert the image into a format OpenCV can use
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
    # Display the image
    cv2.imshow(win_name1, frame)
    cv2.imshow(win_name2, frame2)
    key = cv2.waitKey(1)
    if key == ord('q'):
        alive = False
        break
    elif key == ord('s'):
        cv2.imwrite('screenshot.png', frame)
        #takes a snapshot



cam1.stop()
cv2.destroyAllWindows()