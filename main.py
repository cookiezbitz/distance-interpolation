"""SETTINGS AND VARIABLES ________________________________________________________________"""

## This is intended to work on linux systems
import numpy
import cv2
import matplotlib.pyplot as plt
from time import sleep
import os
import sys
from picamera2 import Picamera2, Preview



# Initialize Picamera2
cam1 = Picamera2()
preview_config = cam1.create_preview_configuration()
cam1.configure(preview_config)
cam1.start()

alive = True
win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)



#source = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while alive:
    # Capture an image with picamera2
    frame = cam1.capture_array()
    # Convert the image into a format OpenCV can use
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # Display the image
    cv2.imshow(win_name, frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        alive = False
        break
    elif key == ord('s'):
        cv2.imwrite('screenshot.png', frame)
        #takes a snapshot



cam1.stop()
cv2.destroyAllWindows()