import cv2 as cv
#import os

camera = cv.VideoCapture(0)
ip = "http://10.206.49.37:8080/video"
camera.open(ip)

parent_dir = "C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection/pole/negative"
count = 1749
while count<2000:
    status, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    resized_img = cv.resize(gray, (1000,1000))
    #location = 'C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection'
    cv.imwrite(parent_dir+'/negimg'+str(count+1)+'.jpg',resized_img)
    count=count+1