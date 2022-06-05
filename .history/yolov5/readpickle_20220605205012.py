import pickle
import cv2
import numpy as np
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


# img_source = "yolov5/bouraouiTest.jpg"
img_source = "yolov5/boratest.png"
img = cv2.imread(img_source)
for i in regions:
    # img = cv2.polylines(img, [i], True, (0,255,0), 1)
    img = cv2.fillPoly(img, pts=[i], color=(0, 255, 0))

# Displaying the image
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break





