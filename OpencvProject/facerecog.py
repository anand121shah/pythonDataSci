import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Specify the camera index (e.g., 0 for the laptop camera)
camera_index = 1

cap = cv2.VideoCapture(camera_index)

while True:
    ret, img = cap.read()
    cv2.imshow('Press ESC key to close this window', img)
    k = cv2.waitKey(30)

    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
