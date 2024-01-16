# import the opencv library
import cv2
import objects
from PIL import Image
import numpy as np

# rescaling function
def rescaleFrame(frame , scale):
   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width,height)

   return cv2.resize(frame , dimensions , interpolation=cv2.INTER_AREA)

# loading lite model
model = 'C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection/android.tflite'
options = objects.ObjectDetectorOptions(
      num_threads=4,
      score_threshold=0.5,
)
detector = objects.ObjectDetector(model_path=model, options=options)

# define a video capture object
ip = "http://192.168.220.212:8080/video"
vid = cv2.VideoCapture(ip)


while(True):
  
 # Capture the video frame by frame
 ret, frame = vid.read()
 
 frame = rescaleFrame(frame , scale=0.35)
 gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 image = Image.open(gray_frame).convert('RGB')
 image.thumbnail((512, 512), Image.ANTIALIAS)
 image_np = np.asarray(image)
 # Run object detection estimation using the model.
 detections = detector.detect(image_np)
 
 # Draw keypoints and edges on input image
 image_np = objects.visualize(image_np, detections)

 cv2.imshow('Pole Detector', image_np)
 
 if cv2.waitKey(1) & 0xFF == ord('f'):
  break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
