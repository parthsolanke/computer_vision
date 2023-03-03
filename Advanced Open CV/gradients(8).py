import cv2 as cv
import numpy as np

img = cv.imread('Photos/CAT_2.jpg')
cv.imshow('org img', img)

# need to convert the image to grayscale in order to get gradients
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# the gradient measures the change in pixel intensity in a given direction
# By estimating the direction or orientation along with the magnitude that is how strong the change in direction is
# we are able to detect regions of an image that look like edges
#  image gradients are estimated using kernels just like in smoothing and blurring
# goal here is to find the change in direction to the central pixel in both the x and y direction

# 1. Laplacian method to calculate gradient
# when a pixel intensity is increasing from black to white then it is considered positive gradient/slope
# similarly when a pixel intensity decreases from white to black then it is considered negative gradient/slope
# here the gradient is calculated via Laplacian method the 2nd parameter represents data depth 
lap = cv.Laplacian(gray, cv.CV_64F)
# in some cases the gradients might be negative but the pixel intensity value cant be negative
# hence we taek teh absolute value of the gradients of lap and convert it into an image specific datatype 'uint8'
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# 2. Sobel method for gradient calculation
# sobel computes gradients in x and y direction
# for gradients x direction
# for x gradients we need pass the x direction as dx=1
sobelx = cv.Sobel(gray, cv.CV_64F, dx=1, dy=0)
cv.imshow('Sobel X', sobelx)
# for gradients in y direction
# for y gradients we need pass the y direction as dy=1
sobely = cv.Sobel(gray, cv.CV_64F, dx=0, dy=1)
cv.imshow('Sobel Y', sobely)
# combining gradients in x and y direction by using bitwise or operation
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

# canny edges
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)