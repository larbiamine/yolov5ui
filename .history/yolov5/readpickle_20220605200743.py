import pickle
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions)

print(type(regions))