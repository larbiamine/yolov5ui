import torch
import cv2 as cv
import numpy as np
model = torch.hub.load('yolov5','custom', path='yolov5/bouraoui.pt', force_reload=True, source='local')

predictions = model("yolov5/bouraouiTest.jpg")

# print(predictions)

# labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()

table = predictions.pandas().xyxy[0]
table = table.reset_index() 
# print(table)


img = np.zeros((512,512,3), np.uint8) 


for index, row in table.iterrows():
    print(row['xmin'], row['ymin'])
    cv.rectangle(img,(int(row['xmin']),int(row['ymin'])),(int(row['xmax']),int(row['ymax'])),(0,255,0),3)


cv.imshow('img',img)
cv.waitKey(0)




# print(labels)
# print(cord_thres)

