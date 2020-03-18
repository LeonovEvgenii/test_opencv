import cv2

cam1 = cv2.VideoCapture(2)
cam2 = cv2.VideoCapture(4)

# save video one camera
# codec = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('captured.avi',codec, 25.0, (640,480))

while 1:
	ret, frame1 = cam1.read()
	ret, frame2 = cam2.read()
	cv2.imshow('window1', frame1)
	cv2.imshow('window2', frame2)
	ch = cv2.waitKey(5)
	if ch == 27:
		break

# out.release()
cam1.release()
cam2.release()
cv2.destroyAllWindows()

