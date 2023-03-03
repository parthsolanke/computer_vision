import cv2 as cv
import numpy as np

img = cv.imread('Photos/DOG_2.jpg')
cv.imshow('Org_IMG',img)

# Split function in open cv spligts the image in 3 color channels
# the split and created images are nothing but intensities of b,g,r color in the image 
# the arrays are returned in the b,g,r order
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Here the 1st 2 arguments of shape of the b,g,r image is the smame  as the original image 
# but the 3rd parameter of the image which represents the no. of color channels is diffrent 
# as the no of color channels in keach of the split image is only one 
print('orignal shape:', img.shape)
print('blue shape:', b.shape)
print('green shape:', g.shape)
print('red shape:', r.shape)

# We can merge the split color channels into one by using the merge fn
# using merge fn we can get bacj the original image
# teh parameter to pass in is the list of color channels in the order b,g,r
merge = cv.merge([b,g,r])
cv.imshow('Merged', merge)

# By using the merge fn we can visualize the color channels better
# 1st we have to create an blank image of same shape as the org image 
# only the 1st 2 shaoe arguments which are the height and width of the image should be same 
# the 3rd argument is of the color channels hence cant  be passed to the blank image 
# [:2] represents the 1st 2 args of the img only
blank = np.zeros(img.shape[:2], dtype='uint8')
# here by using the merge fn we can visualize each color channel seperately
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('B', blue)
cv.imshow('G', green)
cv.imshow('R', red)

cv.waitKey(0)
