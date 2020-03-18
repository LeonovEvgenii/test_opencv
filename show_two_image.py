import cv2
import datetime

cam1 = cv2.VideoCapture(2)
cam2 = cv2.VideoCapture(4)

frame1 = cam1.read()[1]
frame2 = cam2.read()[1]

now = datetime.datetime.now()

cv2.imwrite(now.strftime('/tmp/%M%S_right.jpg'), frame1)
cv2.imwrite(now.strftime('/tmp/%M%S_left.jpg'), frame2)