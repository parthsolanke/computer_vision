from turtle import shape
import cv2 as cv
import numpy as np 

# creating a blank image to draw on & storing it in variable "blank"
# here np.zeros is a function in numpy used to generate an array containing zeros
# np.zeros when have to display an image takes input of shape in this case which is 500x500 = height x width x colour channel
# the 3 input represents 3 channels of colour "BLUE,GREEN,RED" arbitarily it is all black
# we also have to pass data type of the array of zeroes in np.zeroes in this case it is "uint8"
# "uint8" is a datatype generelly representing graphics
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank' , blank)

# 1.painting the blanke image a certain colour
# here by "[:]" we are refrencing all the pixels
# 0,255,0 is the B,G,R colour channel value 255 representing the highest value and 0 the lowest
# as 255 is value of colour cahnnel green out of 3 hence the whole image will be green
blank[:] = 0,255,0
cv.imshow('Blank_Green' , blank)

# by giving parameters to the blank1 variable we can colore only a specific area of pixels
blank1 = np.zeros((500,500,3),dtype='uint8')
blank1[ 200:300 , 300:400 ] = 0,255,0
cv.imshow('Blank_Green_p' , blank1)

# for drawing a rectangle we use a function
# the function takes an image as input and coordinate of points 1 to 2 where we wanna draw the rectangle
# here "(0,0) , (200,200)" means pixels from origin to a certain point
# here "(0,255,0)" basically says of which colour the rectangle should be 
# by "thickness = _ " desired thickness can be given thickness = cv.FILLED or thickness = -1 is used to fill up any shape
blank2 = np.zeros((500,500,3),dtype='uint8')
# colouring blank2 white
#blank2[:] = 255,255,255
cv.rectangle(blank2 , (0,0) , (250,250) , (0,255,0) , thickness=2)
cv.imshow('blank_rectangle' , blank2)

# Drawing a circle 
# have to pass the image to write on 
# have to pass the desired location of center of the circle
# here  (250,250) is the center of the circle 
# 50 is the radius 
# (0,0,255) is for the desired color 
# and the thickness of the circle is 2 
cv.circle(blank2 , (250,250) , 50 , (0,0,255) , thickness=2 )
cv.imshow('Circle on blank' , blank2)

# Drawing  line 
# here coordinate (250,250) is same as (blank3.shape[1]//2 , blank3.shape[0]//2) where [1] representing height and [0] representing width 
# '//' is a division operator returning float value where '/' is division operator returning whole value
cv.line(blank2 , (0,0) , (blank2.shape[1]//2 , blank2.shape[0]//2)  , (255,0,0) , thickness=3)
cv.imshow('line on blank' , blank2)

# writing text on image
# 3rd parameter are the coordinates where we want to dispaly the text 
# cv.FONT_HERSHEY_PLAIN is for the font of the text we wanna display 
# 1.0 is how much we want the font to sacale with 
# Second last parametere is for the colour of text which is green in this case
# and the last parameter is for thickness
blank [:] = 0,0,0
cv.putText( blank , ' Prediction: 1' , (225,225) , cv.FONT_HERSHEY_SIMPLEX , 1.0 , (0,255,0) , 1)
cv.imshow('Text' , blank)

cv.waitKey(0)

