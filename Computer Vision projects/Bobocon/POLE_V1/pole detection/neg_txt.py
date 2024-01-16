import os 

with open('neg.txt', 'w') as f:
    for filename in os.listdir('C:/Users/Parth Solanke/Documents/dev/OpenCV/Robocon/pole detection/pole/negative'):
        f.write('negative/' + filename + '\n')