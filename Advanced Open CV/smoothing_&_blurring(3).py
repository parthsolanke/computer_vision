import cv2 as cv

img = cv.imread('Photos/DOG_1.jpg')
cv.imshow('Org_IMG', img)

# Averaging
# averaging is a type of blurring in which a kernel size is one of the parameter
# the kernal size specifies the size of matrix which is selected from the top left corner of the image matrix
# this matrix moves from left to right and top to bottom respectively
# in averaging the intensity of the middle pixel of the kernal is changed to the average of the intensity of the surrownding pixels
# hence by blurring the effect can be increased by increasing the kernel size eg (3,3) to (7,7) 
averaging = cv.blur(img, (5,5))
cv.imshow('Average Blur', averaging)

# Gaussian blur
# it is a more natural method providing less bluring than averaging
# works similar to averaging method
# but here insted of considering the surrounding pixel intensity each surroundiing pixel is assigned a weight
# this weight is then averaged out to get blurring effect
# the last parameter is called sigma x which is the pixel deviation on x axis
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('Gaussian Blur', gauss)

# Median blur
# more effective than above techniques in order to reduce noise more effectively
# it works same as averaging but insteadf of averaging the intensity it takes the median of the intensities
# here the kernal size is not tuple as opencv understands the size of the matrix by an integer typep value
median =  cv.medianBlur(img, 5)
cv.imshow('Median Blur', median) 

# Bilateral blurring 
# it is more effective and used in many advanced cv tasks
# other blurring techiniques blurs the img without considering the edges but in bilateral blurring the edges are retained
# the 2nd last parameter of the fn is sigma color which consideres the colour of neighbouring pixel 
# the last parameter is the value of sigmapixel the value represent that pixel intensity of how far pixel should influence the central pixel intensity of the kernal
bilateral = cv.bilateralFilter(img, 5, 35, 100)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)