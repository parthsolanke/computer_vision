import cv2 as cv
import numpy as np

# rescaling function
def rescaleFrame(frame , scale = 0.25):

   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width,height)
   
   return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

raw_img = cv.imread('Photos/CAT_0.jpg')
img = rescaleFrame(raw_img , scale=0.15)
cv.imshow('CAT' , img)

# 1. converting an image to gray scale
# cv.cvtColor() is used to change the colour of the image 
# taking parametaer as the image to process and cv.COLOR_BGR2GRAY for changing the colour to gray 
gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray_CAT' , gray_img)

# 2. bluring an image by using gaussian blur
# done by using cv.GaussianBlur() fn 
# taking parameters of image to process , kernal size(by how much intensity the imag eshould be blured)
# the bluring intensity will increase if the kernal size is increased eg : from (3,3) to (7,7)
# and cv. border default
blur_img = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow('blured' , blur_img)

# 3. Edge cascade used to find edges in the image 
# we are gonna use canny method here 
# we can reduce the no. of edges by sending blured image to thr canny method
# the 3rd and 4th parameter is the threshold values
edged = cv.Canny(img , 125 , 175)
cv.imshow('Edges' , edged)
# reduced amount of edges by using blured image
edged2 = cv.Canny(blur_img , 125 , 175)
cv.imshow('Edges2' , edged2)

# 4. dialate the image by using structuring element in this case which is edges from canny fn
# parameters are the edged image from canny fn and kernal size and the no, of iterations
dialeted_img = cv.dilate(edged2 , (7,7) , iterations=3)
cv.imshow('dialated' , dialeted_img)

# 5. eroding the dialeted image (reversing to get back the structuring element)
# parameters are the dialated image , kernal size , iterations
# if the 2nd and 3rd oarameter are same as of dilated function then we wil get the closest img of thr structuring element
eroded_img = cv.erode(dialeted_img , (7,7) , iterations=3)
cv.imshow('Eroded' , eroded_img)

# 6. Resizing the frame/image
# 1st parameter is the image to resize
# 2nd parameter is the desired window size for the image to resize
# 3rd parameter represents interpolation which is defined as:
# The inlargmentnt or downscaling of the size of the pixels of an image when tried incresing or decreasing the size of the image or frame 
# The last parameter is of the interpolation which takes the method for interpolation eg.: INTER_AREA (used when decresingthe size), INTER_LINEAR/INTER_CUBIC (used when incresing the size, liner is fast and cubic is slower but gives more acuurate results)
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 7. Cropping the image
# image is an array of pixels so we can save some part of an array in another here it is 'cropped'
# '50:200' represents height pixels from 50 to 200 and '200:400' represents the width pixels from 200 to 400 
# The origin being at the left uppermost point of the image
cropped = img[50:200,200:400]
cv.imshow('Cropped' , cropped)

##################################################################################################################################################################################################################################################################

# @. CONTOUR DETECTION (contures are the edges found in an image. They are diffrent than canny edges as the use cascade to detect the edges)

# 1. Canny edge detector
# first of all we have to convert the image into grayscale
# then we blur the image
# and then by using canny function we get the edges of the image  
image = cv.imread('Photos/MAN_1.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(image , (5,5) , cv.BORDER_DEFAULT)
canny_edges = cv.Canny(blur , 125 , 175)
cv.imshow('canny',canny_edges)

# 2. Contours
# The function 'cv.findContures' returns the number of all the contures found in a form of a python list which in this case is stored in var contures
# and the function also returns the hierarchieal representation of contures found which is in this case stored in 'hierarchies'
# 1st parameter for the function is the structural element 'canny_edges,
# 2nd parameter is the can be RETR_TREE (for the hierarchieal contures), RETR_EXTERNAL (for the external contoures), RETR_LIST (for all the contoures)
# 3rd parameter is the contour approximation method
contours, hierarchies = cv.findContours(canny_edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countres found in canny edged image')

# 3. Another method to create the structural element other than the canny edges
# we can also create the structural element by getting the threshold (converting the image into binary)
# it looks at an image and binarizes that image (converring it into 2 colours)
# the 1st parameter is the image we wanna binarize
# 2nd parameter is the lowest intensity of an pixel below which we want the value of the pixel as black or o
# 3rd parameter is the max value of the intensity of the pixel if the intensity of the pixel is above 225 it is going to be set as white 
ret, thresh = cv.threshold(gray, 125, 225, cv.THRESH_BINARY)
cv.imshow('binarized', thresh)
contours, hierarchies = cv.findContours(thresh     , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countres found in thresholded image')

# 4. visualizing countours 
# 1st have to create blank image of the same dimensions as the original using numpy 
# 2nd now using draw Countours function we can visualize the deected contours
# the function takes parameters an image to draw on, the list fo detected countours
# the 3rd parameter specifies how many contours we wanna display (-1 menmas we wantr to display all the contours)
# the 4th parameter is the color of the contours and then the thickness of the contours
blank = np.zeros(image.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Countours", blank)


cv.waitKey(0)