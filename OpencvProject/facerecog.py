import cv2


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')



cap = cv2.VideoCapture(0)

while True:

	ret, img = cap.read()

	cv2.imshow('video', img)

	k = cv2.waitKey(30)

	if k == 27: # press 'ESC' to quit

		break