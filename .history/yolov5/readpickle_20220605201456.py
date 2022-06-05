import pickle
import cv2
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


img_source = "yolov5/bouraouiTest.jpg"
img = cv2.imread(img_source)
cv2.polylines(img, regions, True, (0,255,0), 2)
