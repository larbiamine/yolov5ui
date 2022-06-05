import torch
import cv2 as cv
model = torch.hub.load('yolov5','custom', path='yolov5/bouraoui.pt', force_reload=True, source='local')

predictions = model("yolov5/bouraouiTest.jpg")

print(predictions)

# labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()

print(predictions.pandas().xyxy[0])

img = np.zeros((512,512,3), np.uint8) 
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# print(labels)
# print(cord_thres)