import torch
import cv2 as cv
import numpy as np
model = torch.hub.load('yolov5','custom', path='yolov5/bouraoui.pt', force_reload=True, source='local')
img_source = "yolov5/bouraouiTest.jpg"
predictions = model(img_source)

# print(predictions)

# labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()

table = predictions.pandas().xyxy[0]
table = table.reset_index() 
# print(table)


img = np.zeros((640,640,3), np.uint8) 


for index, row in table.iterrows():
    x = (int(row['xmax']) + int(row['xmin'])) / 2
    y = (int(row['ymax']) + int(row['ymin'])) / 2

    print("Point: ")
    print(str(x), str(y))
    cv.rectangle(img,(int(row['xmin']),int(row['ymin'])),(int(row['xmax']),int(row['ymax'])),(0,255,0),3)

import pickle
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions)

cv.imshow('img',img)
cv.waitKey(0)




# print(labels)
# print(cord_thres)

