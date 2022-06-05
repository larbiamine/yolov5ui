import torch

model = torch.hub.load('/Users/macmini04/Documents/yolov5','custom', path='best.pt', force_reload=True, source='local')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='nicebest.pt') 
predictions = model("nicebest.jpg")


labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()


print(labels)