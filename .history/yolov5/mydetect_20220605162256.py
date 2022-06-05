import torch

model = torch.hub.load('yolov5','custom', path='yolov5/bouraoui.pt ', force_reload=True, source='local')

predictions = model("yolov5/nicebest.jpg")

print(predictions)

# labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()

# print(predictions.pandas().xyxy[0])

# print(labels)
# print(cord_thres)