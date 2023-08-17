import cv2
print(cv2.__version__)
dispW=1280
dispH=960
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=21/1 ! nvvidconv flip-method=2 ! video/x-raw, width=480, height=680, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
while True:
    ret, frame=cam.read()
    cv2.imshow('piCam', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release
cv2.destroyAllWindows()
#'+str(flip)+'