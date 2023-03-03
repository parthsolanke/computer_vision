import cv2 as cv

img = cv.imread('Photos/CAT_3.jpg')
cv.imshow('org img', img)

# before thresholding the image we have to convert it into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray img', gray)

# in thresholding the a threshold value is set
# if any pixel intensity value exists below threshold value then it is converted into 0 orblack
# if any pixel intensity value exists above threshold value then it is converted into 255 or white
# this is called binarizing the image as it is converted into a binary image

# 1. Simple Thresholding
# 2nd parameter specifies the value of threshold if a pixel intensity value exists above that the values of pixel will be converted to max value 
# 150 is the threshold value can be modified
# the 3rd parameter is the max value which is 255 can be modified 
# 3rd specifies the type of thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)
print(thresh)
# here we have inversed the thresholding by changing the type in 3rd parameter
inv_threshold, inv_thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple inverse threshold', inv_thresh)

# 2. Adaptive Thresholding
# 2nd parameter is the maximum value that can be assigned to a pixel
# 3rd parameter is adaptive method which decides how threshold value is calculated
# there are diffrent types of adaptive method such as cv.ADAPTIVE_THRESH_MEAN_C and cv.ADAPTIVE_THRESH_MEAN_C
# in cv.ADAPTIVE_THRESH_MEAN_C the threshold Value is (Mean of the neighbourhood area values – constant value), in other words it is the mean of the blockSize×blockSize neighborhood of a point minus constant
# in cv.ADAPTIVE_THRESH_GAUSSIAN_C the threshold Value is (Gaussian-weighted sum of the neighbourhood values – constant value), in other words, it is a weighted sum of the blockSize×blockSize neighborhood of a point minus constant
# blocksize is size of a pixel neighborhood that is used to calculate a threshold value
# the constant value is teh value that is subtracted from the mean or weighted sum of the neighbourhood pixels
adp_thresh_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive mean threshold', adp_thresh_mean)
# here we inversed the thresholding by changing the threshold type for mean thresholding
adp_thresh_mean_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adaptive inverse mean threshold', adp_thresh_mean_inv)
# here we calclulate the threshold value using cv.ADAPTIVE_THRESH_GAUSSIAN_C method
adp_thresh_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive gauss threshold', adp_thresh_gauss)
# here we inversed the thresholding by changing the threshold type for gauss thresholding
adp_thresh_gauss_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adaptive inverse gauss threshold', adp_thresh_gauss_inv)

cv.waitKey(0)