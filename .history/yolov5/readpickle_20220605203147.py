import pickle
import cv2
import numpy as np
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


pts = np.array([
        [ 930* 0.216 ,  620* 0.385],
       [ 829* 0.216,  703* 0.385],
       [1016* 0.216,  718* 0.385],
       [1104* 0.216,  630* 0.385]],)
pts = pts 
pts = np.int32([pts])
#y 0.385
#x 0.216
img_source = "yolov5/bouraouiTest.jpg"
img = cv2.imread(img_source)
img = cv2.polylines(img, [pts], True, (0,255,0), 1)

# Displaying the image
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break





