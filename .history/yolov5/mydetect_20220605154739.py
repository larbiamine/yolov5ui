import torch

model = torch.hub.load('yolov5','custom', path='yolov5/nicebest.pt', force_reload=True, source='local')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='nicebest.pt')  
# model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='nicebest.pt') 
predictions = model("yolov5/nicebest.jpg")


labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()


print(labels)