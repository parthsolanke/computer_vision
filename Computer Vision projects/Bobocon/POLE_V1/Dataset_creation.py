import cv2 as cv
import os

#argument 0 is given to use the default camera of the laptop
camera = cv.VideoCapture(0)
#Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()
    
#creating a list of lables "You could add as many you want"
Labels = ["One","Two","Three","Four","five","Six","Seven","Eight","Nine"]
#Now create folders for each label to store images
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)
        
for folder in Labels:
    #using count variable to name the images in the dataset.
    count = 0
    #Taking input to start the capturing
    print("Press 's' to start data collection for" + folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()
    #clicking 200 images per label, you could change as you want.    
    while count<200:
        #read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        #convert the image into gray format for fast caculation
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #display window with gray image
        cv.imshow("Video Window",gray)
        #resizing the image to store it
        gray = cv.resize(gray, (180,120))
        #Store the image to specific label folder
        cv.imwrite('C:/Users/HP/Documents/AnacondaML/'+folder+'/img'+str(count)+'.png',gray)
        count=count+1
        #to quite the display window press 'f'
        if cv.waitKey(1) == ord('f'):
            break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()