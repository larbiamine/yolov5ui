import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='./runs/train/exp6/weights/best.pt')
model = model.autoshape()  # for PIL/cv2/np inputs and NMS

from PIL import Image

# Images
img1 = Image.open('a.jpg')
img2 = Image.open('b.jpg')
imgs = [img1, img2]  # batched list of images

# Inference
result = model(imgs, size=640)  # includes NMS
result.print()