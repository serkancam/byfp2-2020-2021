import cv2
cam  = cv2.VideoCapture(0)
while True:
	ret,img = cam.read()
	cv2.imshow("yuz",img)
	if cv2.waitKey(25)& 0xFF ==ord('q'):
		cam.release()
		cv2.destroyAllWindows()