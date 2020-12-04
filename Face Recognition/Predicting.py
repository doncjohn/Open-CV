import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
id=0
#font=cv2.cv2.InitFont(cv2.cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
#cv2.putText(im, str(Id), (x,y+h), fontface, fontscale, fontcolor)
while(True):
    ret,img=cam.read()
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        if id==2:
            id='Don C John'
        elif id==3:
            id='Bhavana'
        cv2.putText(img,str(id),(x,y+h),fontface,fontscale,fontcolor)
    cv2.imshow('Face',img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()