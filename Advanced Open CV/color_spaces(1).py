import cv2 as cv
import matplotlib.pyplot as plt

# open cv by default use BGR color space 
# the read imag ewill be stored in BGR color space 
img = cv.imread('Photos/WOMEN_1.jpg')
cv.imshow("Original", img)
# The same BGR image in RGB color space looks diffrent
# as all of the colors will be inverted in the RGB color space
# uncomment following to run
#plt.imshow(img)
#plt.show()

# BGR to RGB
# here the follwing changed image will be inverted in cv2
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# but in pyplot the image will be not inverted as now exists in RGB space
# uncomment following to run
#plt.imshow(rgb)
#plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# HSV to BGR 
# by the same following way one can convert LAB to BGR
h_to_b = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', h_to_b)

cv.waitKey(0)

# Note: cant convert HSV to Grayscale directly hence 1st have to convert into BGR then into Grayscale