import cv2 as cv
import os

camera = cv.VideoCapture(0)
ip = "http://192.168.41.23:8080/video"
camera.open(ip)

if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()
    
Labels = ["positive","negative"]

# Parent Directory path
parent_dir = "C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection"

for label in Labels:
    # Path
    paths = os.path.join(parent_dir, label)
    if not os.path.exists(label):
        os.mkdir(paths)
        
for folder in Labels:
    count = 0
    print("Press 's' to start data collection for" + folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input...")
        exit()    
    while count<500:
        status, frame = camera.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        resized_img = cv.resize(gray, (24,24))
        #location = 'C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection'
        cv.imwrite(parent_dir+folder+'/img'+str(count)+'.jpg',resized_img)
        count=count+1
        if cv.waitKey(1) == ord('f'):
            break