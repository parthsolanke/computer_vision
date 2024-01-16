import cv2 as cv
path = r'tets_data\pole_vid (2).mp4'
destination = r'train'
cap = cv.VideoCapture(path)
count =  0
while count<50:
    ret, frame = cap.read()
    frame = cv.resize(frame, (300,500))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    threshold, thresh = cv.threshold(h , 150, 255, cv.THRESH_BINARY)
    print(h)
    cv.imshow('t', thresh)
    if not ret:
        break
    # cv.imwrite(destination+'/img'+str(count)+'.png',frame)
    # count += 1
    if cv.waitKey(1) == ord('f'):
        break
    
cap.release()
cv.destroyAllWindows()