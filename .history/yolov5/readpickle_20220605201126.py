import pickle
regions = pickle.load(open('yolov5/regions.p', 'rb'))
print(regions[0])




print(type(regions[0]))