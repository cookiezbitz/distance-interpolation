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
