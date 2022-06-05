import torch
import cv2 as cv
import numpy as np
model = torch.hub.load('yolov5','custom', path='yolov5/bouraoui.pt', force_reload=True, source='local')
img_source = "yolov5/boratest.png"
predictions = model(img_source)

# print(predictions)

# labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()

table = predictions.pandas().xyxy[0]
table = table.reset_index() 
# print(table)


import pickle
regions = pickle.load(open('yolov5/regions.p', 'rb'))
img_source = "yolov5/boratest.png"
img = cv.imread(img_source)

print(len(regions))
print(len(table))

print(regions)
print(table)

for ((index, row),j) in zip(table.iterrows(), regions):
    print(row['class'])
    if(int(row['class']) == 1 and float(row['confidence']) == 1):
        img = cv.polylines(img, [j], True, (0,0,255), 2)
    else:
        img = cv.polylines(img, [j], True, (0,255,0), 2)

# for index, row in table.iterrows():
#     x = (int(row['xmax']) + int(row['xmin'])) / 2
#     y = (int(row['ymax']) + int(row['ymin'])) / 2

#     print("Point: ")
#     print(str(x), str(y))
#     for i in regions:
#         if(cv.pointPolygonTest(i, (x, y), False) != -1):
#         #if(polygonRect_intersection([int(row['xmin']),int(row['ymin']),int(row['xmax']),int(row['ymax'])], i)):
#             if(row['class'] == "0"):
#                 img = cv.polylines(img, [i], True, (0,0,255), 2)
#             else:     
#                 img = cv.polylines(img, [i], True, (0,255,0), 2)
#     #cv.rectangle(img,(int(row['xmin']),int(row['ymin'])),(int(row['xmax']),int(row['ymax'])),(0,255,0),3)


img = cv.resize(img, (1280, 720))
cv.imshow('img',img)
cv.waitKey(0)




# print(labels)
# print(cord_thres)

