import pickle
import cv2
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])

print(type(regions[0]))


img_source = "yolov5/bouraouiTest.jpg"
img = cv2.imread(img_source)
cv2.polylines(img, regions, True, (0,255,0), 2)

# Displaying the image
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
