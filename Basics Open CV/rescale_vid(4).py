# reading and rescaling videos

import cv2 as cv

# rescaling function
def rescaleFrame(frame , scale = 0.25):
   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width,height)

   return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

# storing video in a variable "capture"
capture = cv.VideoCapture('Videos/Dog.mp4')

# Initialize variables
start_time = cv.getTickCount()
frame_count = 0

# reading the video frame by frame and displaying rescaled video
while True:
    # is true will terminate when there is no frame to read
    isTrue, frame = capture.read()

    # calling rescale function have pass frame & can pass desired scale
    resized_frame = rescaleFrame(frame , scale=0.1)

    # Calculate elapsed time and fps
    elapsed_time = (cv.getTickCount() - start_time) / cv.getTickFrequency()
    fps = frame_count / elapsed_time
  
    # Display fps on frame
    cv.putText(resized_frame, f"FPS: {fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1)

    #cv.imshow('Video',frame)
    cv.imshow('Video',resized_frame)

    # if "f" key is pressed then program will escape from created window
    if cv.waitKey(20) & 0xFF==ord('f'):
        break
    
    # Increment frame count
    frame_count += 1

# relesing all pointers
capture.release()
cv.destroyAllWindows()