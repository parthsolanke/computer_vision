# importing cv2 library 
import cv2 as cv

# storing the desired image in variable named img
img = cv.imread('Photos/DOG_2.jpg')

# displaying stored image in a window
cv.imshow('DOG' , img)

# waiting for any key to be pressed to terminate the program
cv.waitKey(0)

