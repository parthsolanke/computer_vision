import cv2 as cv
import pytesseract

img = cv.imread(r"Computer Vision projects\Optical character recognition\test_img.png")

config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(img, config=config)
print(text)

cv.imshow("Text", img)

cv.waitKey(0)