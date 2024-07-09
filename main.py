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

# Start Condition variables

natrual = True
canny = False
blur = False
faceDetection = False
disparity = False

win_name1 = "Right Camera"
win_name2 = "Left Camera"
filteredImage1 = None
filteredImage2 = None

base_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(base_dir, "lib", "deploy.prototxt")
caffemodel_path = os.path.join(
    base_dir, "lib", "res10_300x300_ssd_iter_140000_fp16.caffemodel"
)


# face detection variables
net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
in_width = 300
in_height = 300
mean = [104, 117, 123]
conf_threshold = 0.7

# Stereo Vision Variables
stereo = cv2.StereoBM.create(numDisparities=16, blockSize=15)


# canny thresholds
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
# matplotlib settings
plt.ion()

cv2.namedWindow(win_name1, cv2.WINDOW_NORMAL)
cv2.namedWindow(win_name2, cv2.WINDOW_NORMAL)

while alive:

    # Capture an image with picamera2
    frame = cam1.capture_array()
    frame2 = cam2.capture_array()
    # Convert the image into a format OpenCV can use
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
    if firstStart:
        filteredImage1 = frame
        filteredImage2 = frame2
        firstStart = False
    # Display the image
    cv2.imshow(win_name1, filteredImage1)
    cv2.imshow(win_name2, filteredImage2)
    key = cv2.waitKey(1)
    if key == ord("q"):
        alive = False
        break
    elif key == ord("s"):
        cv2.imwrite("screenshot.png", frame)
        print("Screenshot saved as screenshot.png")
        # takes a snapshot
    elif key == ord("n"):
        natrual = True
        canny = False
        blur = False
        faceDetection = False
        disparity = False
    elif key == ord("c"):
        natrual = False
        canny = True
        blur = False
        faceDetection = False
        disparity = False

    elif key == ord("b"):
        natrual = False
        canny = False
        blur = True
        faceDetection = False
        disparity = False
    elif key == ord("f"):
        natrual = False
        canny = False
        blur = False
        faceDetection = True
        disparity = False
    elif key == ord("d"):
        natrual = False
        canny = False
        blur = False
        faceDetection = False
        disparity = True

    # ====================================================================
    if natrual:
        filteredImage1 = frame
        filteredImage2 = frame2
    if canny:
        filteredImage1 = cv2.Canny(frame, cannylow, cannyhigh)
        filteredImage2 = cv2.Canny(frame2, cannylow, cannyhigh)
    if blur:
        filteredImage1 = cv2.blur(frame, (5, 5))
        filteredImage2 = cv2.blur(frame2, (5, 5))
    if faceDetection:

        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(
            frame, 1.0, (in_width, in_height), mean, swapRB=False, crop=False
        )
        # blob2 = cv2.dnn.blobFromImage(frame2, 1.0, (in_width, in_height), mean, swapRB=False, crop=False)
        # Run a model
        net.setInput(blob)

        detections = net.forward()

        frame_height = frame.shape[0]
        frame_width = frame.shape[1]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x_left_bottom = int(detections[0, 0, i, 3] * frame_width)
                y_left_bottom = int(detections[0, 0, i, 4] * frame_height)
                x_right_top = int(detections[0, 0, i, 5] * frame_width)
                y_right_top = int(detections[0, 0, i, 6] * frame_height)

                cv2.rectangle(
                    frame,
                    (x_left_bottom, y_left_bottom),
                    (x_right_top, y_right_top),
                    (0, 255, 0),
                )
                label = "Confidence: %.4f" % confidence
                label_size, base_line = cv2.getTextSize(
                    label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
                )

                cv2.rectangle(
                    frame,
                    (x_left_bottom, y_left_bottom - label_size[1]),
                    (x_left_bottom + label_size[0], y_left_bottom + base_line),
                    (255, 255, 255),
                    cv2.FILLED,
                )
                cv2.putText(
                    frame,
                    label,
                    (x_left_bottom, y_left_bottom),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                )

        t, _ = net.getPerfProfile()
        label = "Inference time: %.2f ms" % (t * 1000.0 / cv2.getTickFrequency())
        cv2.putText(frame, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        cv2.imshow("banana", frame)
        filteredImage1 = frame
        filteredImage2 = frame2
    if disparity:
    #    cv2.imwrite("leftAsset.png", frame)
    #    cv2.imwrite("rightAsset.png", frame2)
    #    imgL = cv2.imread("leftAsset.png", cv2.IMREAD_GRAYSCALE)
    #    imgR = cv2.imread("rightAsset.png", cv2.IMREAD_GRAYSCALE)
        gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        stereo = cv2.StereoBM.create(numDisparities=16, blockSize=15)
        disparityComputed = stereo.compute(gray1, gray2)
        #plt.imshow(disparityComputed, "gray")
        #plt.show()
        
        cv2.imshow("Disparity", disparityComputed)
        # filteredImage2 = stereo.compute(imgL,imgR)

    # print("Disparity")


cam1.stop()
cam2.stop()
cv2.destroyAllWindows()
