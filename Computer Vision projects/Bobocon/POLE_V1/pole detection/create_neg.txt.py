import os

with open('neg.txt', 'w') as f:
    for filename in os.listdir('Robocon/pole detection/pole/negative'):
        f.write('negative/' + filename + '\n')