from turtle import shape
# import the opencv library
import cv2
# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
 # Capture the video frame
 # by frame
 ret, frame = vid.read()
 cv2.namedWindow("Resize", cv2.WINDOW_NORMAL)
 cv2.resizeWindow("Resize", 800, 480)
 # Display the resulting frame
 
 # GREEN
 # Vertical
 cv2.line(frame , (200,200) , (frame.shape[1]-200,200)  , (0,255,0) , thickness=3)
 # Horizontal
 cv2.line(frame , (int(200*2/3),int((200*2+(frame.shape[0]))/3)) , (200,200)  , (0,255,0) , thickness=3)
 cv2.line(frame , (int(((frame.shape[1]-200)*2+frame.shape[1])/3),int((frame.shape[0]+200*2)/3)) , (frame.shape[1]-200,200)  , (0,255,0) , thickness=3)
 
 # ORANGE
 # Vertical
 cv2.line(frame , (int(200*2/3),int((200*2+(frame.shape[0]))/3)) , (int(((frame.shape[1]-200)*2+frame.shape[1])/3),int((frame.shape[0]+200*2)/3))  , (0,165,255) , thickness=3)
 # Horizontal
 cv2.line(frame , (int(200/3),int((200+2*(frame.shape[0]))/3)) , (int(200*2/3),int((200*2+(frame.shape[0]))/3))  , (0,165,255) , thickness=3)
 cv2.line(frame, (int(((frame.shape[1]-200)+2*frame.shape[1])/3),int((frame.shape[0]*2+200)/3)) , (int(((frame.shape[1]-200)*2+frame.shape[1])/3),int((frame.shape[0]+200*2)/3)) , (0,165,255) , thickness=3)
 
 # RED
 # Vertical
 cv2.line(frame , (int(200/3),int((200+2*(frame.shape[0]))/3)) , (int(((frame.shape[1]-200)+2*frame.shape[1])/3),int((frame.shape[0]*2+200)/3))  , (0,0,255) , thickness=3)
 # Horizontal
 cv2.line(frame , (0,frame.shape[0]) , (int(200/3),int((200+2*(frame.shape[0]))/3))  , (0,0,255) , thickness=3)
 cv2.line(frame, (frame.shape[1] , frame.shape[0]) , (int(((frame.shape[1]-200)+2*frame.shape[1])/3),int((frame.shape[0]*2+200)/3)) , (0,0,255) , thickness=3)
 

 cv2.imshow("Resize", frame)
  
 # cv2.imshow('frame', frame)
 # the 'f' button is set as the
 # quitting button you may use any
 # desired button of your choice
 if cv2.waitKey(1) & 0xFF == ord('f'):
  break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
