import pickle
import cv2
import numpy as np
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


pts = np.array([
        [ 930* 0.2 ,  620* 0.385],
       [ 829* 0.2,  703* 0.385],
       [1016,  718],
       [1104 , 630]],)
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




