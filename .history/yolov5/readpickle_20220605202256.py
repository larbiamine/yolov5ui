# import pickle
# import cv2
# import numpy as np
# regions = pickle.load(open('yolov5/regions.p', 'rb'))
# print(regions[0])

# print(type(regions[0]))


# pts = np.array([
#         [ 930,  620],
#        [ 829,  703],
#        [1016,  718],
#        [1104,  630]])

# pts = np.int32([pts])

# img_source = "yolov5/bouraouiTest.jpg"
# img = cv2.imread(img_source)
# img = cv2.polylines(img, [pts], True, (0,255,0), 2)

# # Displaying the image
# while(1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break



# Python program to explain
# cv2.polylines() method

import cv2
import numpy as np

# path
path = "yolov5/bouraouiTest.jpg"

# Reading an image in default
# mode
image = cv2.imread(path)

# Window name in which image is
# displayed
window_name = 'Image'

# Polygon corner points coordinates
pts = np.array([[25, 70], [25, 160],
				[110, 200], [200, 160],
				[200, 70], [110, 20]],
			np.int32)

pts = pts.reshape((-1, 1, 2))

isClosed = True

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.polylines() method
# Draw a Blue polygon with
# thickness of 1 px
image = cv2.polylines(image, [pts],
					isClosed, color, thickness)

# Displaying the image
while(1):
	
	cv2.imshow('image', image)
	if cv2.waitKey(20) & 0xFF == 27:
		break
		
cv2.destroyAllWindows()


