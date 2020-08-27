import cv2
import datetime
from matplotlib import pyplot as plt
import numpy as np

cam1 = cv2.VideoCapture(2)
cam2 = cv2.VideoCapture(4)

frame1 = cam1.read()[1]
frame2 = cam2.read()[1]

frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

now = datetime.datetime.now()

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=13)
disparity = stereo.compute(frame1_gray, frame2_gray)

cv2.line(frame1_gray, (200, 264), (500, 264), 1)
cv2.line(frame1_gray, (320, 100), (320, 400), 1)

cv2.line(frame2_gray, (200, 264), (500, 264), 1)
cv2.line(frame2_gray, (320, 100), (320, 400), 1)

out = np.concatenate((frame1_gray, frame2_gray, disparity), axis = 1)

# cv2.imwrite(now.strftime('/tmp/%M%S_disp.jpg'), disparity)
# cv2.imwrite(now.strftime('/tmp/disp.jpg'), disparity)

# cv2.imwrite('/tmp/left.jpg',  frame1_gray)
# cv2.imwrite('/tmp/right.jpg', frame2_gray)
cv2.imwrite('/tmp/out.jpg',  out)

