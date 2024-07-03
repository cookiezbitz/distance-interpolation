import cv2
import time

source = cv2.VideoCapture("/dev/media0", cv2.CAP_V4L)

# Add a warm-up period
time.sleep(2)  # Wait for 2 seconds

# Optionally, set a specific resolution
source.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
source.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Attempt to capture a frame multiple times
for _ in range(10):
    ret, frame = source.read()
    if ret:
        break
    time.sleep(0.1)  # Wait a bit before retrying

if not ret:
    print(
        "Failed to capture frame after multiple attempts. Camera may not be accessible or index may be incorrect."
    )
else:
    cv2.imshow("Test Frame", frame)
    cv2.waitKey(0)  # Wait for a key press to close the window

source.release()
cv2.destroyAllWindows()
