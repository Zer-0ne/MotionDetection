import cv2 as cv
from  functools import cache


video = cv.VideoCapture(1)
subtractor = cv.createBackgroundSubtractorMOG2(30,20)

while True:
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask',mask)
        if cv.waitKey(5)==ord('X'):
            break
    else:
        video = cv.VideoCapture(0)
cv.destroyAllWindows()
video.release()