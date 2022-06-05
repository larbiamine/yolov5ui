import torch
    
model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='nicebest.pt') 
predictions = model("my_image.png")


labels, cord_thres = predictions.xyxyn[0][:, -1].numpy(), predictions.xyxyn[0][:, :-1].numpy()


print(predictions)