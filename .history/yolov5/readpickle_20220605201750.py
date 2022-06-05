import pickle
import cv2
import numpy as np
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


pts = np.array([
        [ 930,  620],
       [ 829,  703],
       [1016,  718],
       [1104,  630]], np.int32)

img_source = "yolov5/bouraouiTest.jpg"
img = cv2.imread(img_source)
img = cv2.polylines(img, pts, True, (0,255,0), 2)

# Displaying the image
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
