#pip install opencv-python 
import cv2 
# we will use haarcascade for detecting face 
# open cv has many classifiers for detecting faces, smiles etc 

face_cascade 
cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
img= cv2.imread('profile.png') 

# this method work only for grey scale 
# we have to convert our img to gray scale 

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces= face_cascade.detectMultiScale(gray, 1.1,4) 

# rectangle box on faces 
for (x,y,w,h) in faces: 
 
 cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0),2) 
 cv2.imshow('img', img) 
 cv2.waitKey() 