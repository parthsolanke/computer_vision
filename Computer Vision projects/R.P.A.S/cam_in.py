from turtle import shape

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
  
 # Capture the video frame
 # by frame
 ret, frame = vid.read()
 
 # Display the resulting frame
 cv2.line(frame , (200,200) , (frame.shape[1]-200,200)  , (0,0,255) , thickness=3)
 cv2.line(frame , (0,frame.shape[0]) , (200,200)  , (0,255,0) , thickness=3)
 cv2.line(frame, (frame.shape[1] , frame.shape[0]) , (frame.shape[1]-200,200) , (0,250,0) , thickness=3)
 cv2.imshow('frame', frame)
 
 # cv2.imshow('frame', frame)
 # the 'q' button is set as the
 # quitting button you may use any
 # desired button of your choice
 if cv2.waitKey(1) & 0xFF == ord('f'):
  break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
