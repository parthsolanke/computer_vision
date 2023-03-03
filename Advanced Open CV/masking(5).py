import cv2 as cv
import numpy as np

# reading an image to mask
img = cv.imread('Photos/WOMEN_1.jpg')
cv.imshow('ORGimg', img)

# creating blank image to make masks
# should be the same size of image 
blank = np.zeros(img.shape[:2], dtype = 'uint8')

# creating shapes to mask
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (25,25), (200,200), 255, -1)
cv.imshow('circle', circle)
cv.imshow('rectangle', rectangle)

# can create various shapes for masking
shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Shape', shape)

# masking is done by bitwise and 
# takes image to mask on as parameters
# one more parameter is needed which is the shape of the mask
masked_c = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked_c', masked_c)

masked_r = cv.bitwise_and(img, img, mask=rectangle)
cv.imshow('Masked_r', masked_r)

masked_img = cv.bitwise_and(img, img, mask=shape)
cv.imshow('Masked', masked_img)

cv.waitKey(0)
