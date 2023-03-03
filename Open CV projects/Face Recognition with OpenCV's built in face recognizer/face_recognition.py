import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("Open CV projects/Face Recognition with OpenCV's built in face recognizer/haar_face.xml")

people = ['Ben', 'Christian', 'Leonardo', 'Margot', 'Robert', 'Scarlett']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# reading our face recognition yml files
face_recognizer.read("Open CV projects/Face Recognition with OpenCV's built in face recognizer/face_recognizer.yml")

# reading image
img = cv.imread("Open CV projects/Face Recognition with OpenCV's built in face recognizer/val/l&m.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detecting faces in he image using haar cascade classifirs for frontal faces
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 5)


# cropping region of intrest for face recognition
for (x,y,w,h) in faces_rect:
    faces_roi = gray_img[y:y+h,x:x+w]
    
    # getting predection label and probablity confidence
    label, confidence = face_recognizer.predict(faces_roi)
    
    # visualization
    print(f'Label = {people[label]} with a confidence of {confidence:.1f}')
    cv.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 2)
    cv.putText( img , str(people[label]), (x,y-5) , cv.FONT_HERSHEY_SIMPLEX , 0.5 , (255,255,255) , 1)
    
cv.imshow('Detected Face', img)

cv.waitKey(0)