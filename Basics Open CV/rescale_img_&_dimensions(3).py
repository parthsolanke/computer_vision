# 1. reading and rescaling images

import cv2 as cv
         
# rescaling function
def rescaleFrame(frame , scale = 0.25):

   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width,height)
   
   return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

img = cv.imread('Photos/CAT_0.jpg')

rescaled_img = rescaleFrame(img , scale=0.15)

cv.imshow('Cat', rescaled_img)

# 2. following is the code get dimensions of the frame/image
 
frame = cv.imread('Photos/DOG_2.jpg')

# Storing dimensions of image in a variable 
dimensions = frame.shape

# height, width, number of channels in frame
height = frame.shape[0]
width = frame.shape[1]
channels = frame.shape[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

cv.waitKey(0)
