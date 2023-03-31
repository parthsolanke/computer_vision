import os
import cv2 as cv
import numpy as np
import time

# path for train directory & working directory
TRAIN_DIR = r"Open CV projects/Face Recognition with OpenCV's built in face recognizer/train"
WDIR = r"Open CV projects/Face Recognition with OpenCV's built in face recognizer"

# storing the names of persons in a list
people = []
for i in os.listdir(TRAIN_DIR):
    people.append(i)
# printing created list
print('List of classes:', people)

# loading haar cascade to detect faces for training
haar_cascade = cv.CascadeClassifier("Open CV projects/Face Recognition with OpenCV's built in face recognizer/haar_face.xml")

# features is the image array of faces 
features = []
# labels is the label of each class
labels = []
        
# creating the train function aim is to get features and labels
def create_train():
    for person in people:
        # storing the path of directories in TRAIN_DIR
        path = os.path.join(TRAIN_DIR,person)
        # getting the index of the folders in the list which is exactly
        label = people.index(person)
        
        for img in os.listdir(path):
            # storing the image path
            img_path = os.path.join(path,img)
            # reading the image
            img_array = cv.imread(img_path)
            gray_img = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            # using haar cascade to detect faces 
            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=10)
            
            # cropping the detected face in the image 
            for (x,y,w,h) in faces_rect:
                # storing the detected face in a variable
                faces_roi = gray_img[y:y+h, x:x+w]
                # appending the cropped region to feature
                features.append(faces_roi)
                # appending the corresponding label to the labels list
                labels.append(label)

# calling function to get the features and labels list
create_train()

# creatig numpy arrays of features and labels for passing parameters to train instance
features = np.array(features, dtype='object')
labels = np.array(labels)

# instantiatiing opencv's built in recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

print('Training face recognizer...', end='')
start_time = time.time()

# with the features and labels list trainnig opencv's built in face recognizer 
face_recognizer.train(features, labels)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Done! Took {elapsed_time} seconds')

# changing directory to working directory
os.chdir(WDIR)

# saving the trained face recognizer in a yml file
face_recognizer.save('face_recognizer.yml')

# saving the features and labels
np.save('features.npy', features)
np.save('labels.npy', labels)

# going back to original directory
os.chdir('../..')