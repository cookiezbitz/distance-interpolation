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
firstStart = True
win_name1 = "Right Camera"
win_name2 = "Left Camera"
filteredImage1 = None
filteredImage2 = None

#canny thresholds
cannylow = 100
cannyhigh = 200

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
    if(firstStart):
        filteredImage1 = frame
        filteredImage2 = frame2
        firstStart = False
        
    # Capture an image with picamera2
    frame = cam1.capture_array()
    frame2 = cam2.capture_array()   
    # Convert the image into a format OpenCV can use
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
    # Display the image
    cv2.imshow(win_name1, filteredImage1)
    cv2.imshow(win_name2, filteredImage2)
    key = cv2.waitKey(1)
    if key == ord('q'):
        alive = False
        break
    elif key == ord('s'):
        cv2.imwrite('screenshot.png', frame)
        print("Screenshot saved as screenshot.png")
        #takes a snapshot
    elif key == ord('n'):
        filteredImage1 = frame
        filteredImage2 = frame2
    elif key == ord('c'):
        filteredImage1 = cv2.Canny(frame, cannylow, cannyhigh)
        filteredImage2 = cv2.Canny(frame2, cannylow, cannyhigh)
    elif key == ord('b'):
        filteredImage1 = cv2.blur(frame, (5, 5))
        filteredImage2 = cv2.blur(frame2, (5, 5))

        



cam1.stop()
cv2.destroyAllWindows()