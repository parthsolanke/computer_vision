import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/MAN_2.jpg')
cv.imshow('org img', img)

# 1. calculating histogram for gray scaled image
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray_image)

# we can use calcHist() fn to compute  the histogram
# the input parameters are a list of the images for which we want to calculate histogram for
# here we only have one image to calculate histogram for one image we are passing one image only
# the second parameter is for the index of list of color channels we wanna claculate histogram for
# in this case it is just [0] as we have no color channel 
# the 3rd parameter specifies mask which is used to calculate histogram of a specific area of an image
# the 4th is histsize which is no of bins which is to divide the entire range of values into a series of intervals and then count how many values fall into each interval
# the histsize is a list here we set it to [256]
# the 5th parameter is the range of all the possible pixel values 
gray_hist = cv.calcHist([gray_image], [0], None, [256], [0,256])
# using matplotlib to plot a graph
# uncomment following to run
# plt.figure()
# plt.title('Gray Histogram')
# plt.xlabel('Bins')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# 2. plotting histogram for a specific area of an image
# 1st we have to create a mask then get the values for masked region
blank = np.zeros(gray_image.shape[:2], dtype='uint8')
circle_mask = cv.circle(blank, (gray_image.shape[0]//2,gray_image.shape[0]//2), 50, 255, -1)
# calculating histogram values but now the 3rd parameter is the masked area of which we want histogram values 
# the calcHist fn takes bitwise and of the mask and the image in order to get the pixel intensities if that specific area
mask_hist = cv.calcHist([gray_image], [0], circle_mask, [256], [0,256])
# for visualization let us display the masked image using bitwise and
masked_img = cv.bitwise_and(gray_image, gray_image, mask=circle_mask)
cv.imshow('Masked image', masked_img)
# using matplotlib to plot a graph
# uncomment following to run
# plt.figure()
# plt.title('Masked Histogram')
# plt.xlabel('Bins')
# plt.ylabel('no. of pixels')
# plt.plot(mask_hist)
# plt.xlim([0,256])
# plt.show()

# 3. histogram computation for all color channels
# creating a list of color channels 
colors = ('b', 'g', 'r')
# initialising the figure with title and axis quantities
# uncomment following to run
'''
plt.figure()
plt.title('color Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
'''
# using a for loop in order to calculate histogram values for each channel in the list
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], None, [256], [0,256])
    # plotting the values for each color one by one in each iteration
    # uncomment following to run
    '''
    plt.plot(color_hist, color = col)
    '''
    # setting the x-limit for each color
    # uncomment following to run
    '''
    plt.xlim([0,256])
    '''
# uncomment following to run
'''
plt.show()
'''

cv.waitKey(0)