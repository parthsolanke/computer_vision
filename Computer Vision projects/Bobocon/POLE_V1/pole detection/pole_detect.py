# import the opencv library
import cv2

# rescaling function
def rescaleFrame(frame , scale):
   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width,height)

   return cv2.resize(frame , dimensions , interpolation=cv2.INTER_AREA)

# define a video capture object
vid = cv2.VideoCapture(0)
ip = "http://192.168.218.203:8080/video"
vid.open(ip)

#(text_width, text_height), _ = cv2.getTextSize('Pole', cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)


# loading cascade
haar_cascade = cv2.CascadeClassifier('C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection/pole_cascade_v3.xml')

while(True):
  
 # Capture the video frame by frame
 ret, frame = vid.read()
 
 frame = rescaleFrame(frame , scale=0.35)
 gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
 frame_rectangle = haar_cascade.detectMultiScale(gray_frame, scaleFactor = 1.1, minNeighbors = 25)
 
 for (x,y,w,h) in frame_rectangle :
    #bounding box
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,0), thickness = 2)
    #text box
    cv2.rectangle(frame, (x-1,y-20), (x+34,y), (0,0,0), -1)
    #text
    cv2.putText( frame , 'pole' , (x,y-5) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (255,255,255) , 1)
 # Display the resulting frame
 cv2.imshow('Pole Detector', frame)
 
 if cv2.waitKey(1) & 0xFF == ord('f'):
  break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
