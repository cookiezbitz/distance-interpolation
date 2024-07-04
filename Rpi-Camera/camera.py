# This portion of the code would only work on a raspberry pi with the picamera module installed
# This code is used to capture images from two cameras simultaneouslyq
from picamera2 import Picamera2, Preview
from time import sleep

duration = 90
cam1 = Picamera2(0)
cam2 = Picamera2(1)
cam1.start_preview(Preview.QTGL)
cam2.start_preview(Preview.QTGL)
cam1.start()
cam2.start()
sleep(duration)
cam1.close()
cam2.close()
