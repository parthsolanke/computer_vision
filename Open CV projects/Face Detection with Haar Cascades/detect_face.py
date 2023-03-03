import cv2 as cv

img = cv.imread('Open CV projects/Face Detection with Haar Cascades/Einstein.jpg')

# haar cascade detections dosent depend on the color of the image hence gray csaling the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# reading the xml file for haar cascade
haar_cascade = cv.CascadeClassifier('Open CV projects/Face Detection with Haar Cascades/haar_face.xml')

# detecting the faces and getting the list of rectangle coordinates of the detected faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(f'No. faces found = {len(faces_rect)}')

# visualizing the detections
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 1)
cv.imshow('Detected faces', img)

cv.waitKey(0)