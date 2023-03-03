# including cv2 library
import cv2 as cv

# storing desired video filr in a variable named capture
capture = cv.VideoCapture('Videos/glitch.mp4')

# Initialize variables
start_time = cv.getTickCount()
frame_count = 0

# reading the video frame by frame 
while True :
    isTrue , frame = capture.read()
    
    if not isTrue:
        break 
    
    # Calculate elapsed time and fps
    elapsed_time = (cv.getTickCount() - start_time) / cv.getTickFrequency()
    fps = frame_count / elapsed_time
    
    # Display fps on frame
    cv.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1)

    # displaying the vid frame by frame after being read
    cv.imshow('Video' , frame )

    # if key "d" is pressed then the loop will get terminated 
    if cv.waitKey(20) & 0xFF==ord('f') :
        break
    
    # Increment frame count
    frame_count += 1

#releasing all pointers and clearing memory
capture.release()
cv.destroyAllWindows()