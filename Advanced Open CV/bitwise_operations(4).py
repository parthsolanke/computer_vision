import cv2 as cv
import numpy as np

# bitwise operator operate in a binary manner

blank = np.zeros((200,200), dtype='uint8')

# here the last parameter represents that teh whole rectangel should be filled with the specified color 
# in this case the color is 255 menaing white the max value for all channles
# here we are making copies of the blank frame so we get diffrent canvas to draw diffrent stuff
rectangle = cv.rectangle(blank.copy(), (15,15), (185,185), 255, -1)
circle = cv.circle(blank.copy(), (100,100), 100, 255, -1)
cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# 1. Bitwise and returns only the intersecting parts 
# takes parameter as images of which intersecting region is to be found
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("and", bitwise_and)

# 2. Bitwise or returns both intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('or', bitwise_or)

# 3. Bitwise xor returns non intersecting regions 
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bitwise_xor)

# 4. bitwise not returns region which is excludib=ng the input parameter's region
bitwise_not_c = cv.bitwise_not(circle)
bitwise_not_r = cv.bitwise_not(rectangle)
cv.imshow('not_circle', bitwise_not_c)
cv.imshow('not_rectangle', bitwise_not_r)

cv.waitKey(0)
