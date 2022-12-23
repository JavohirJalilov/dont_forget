# import cv2
# import numpy as np
# import torch
# import detect
# import processing
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('MacOSX')
# #Read video
# fname = 'mouse.jpg'
# image = cv2.imread(fname)

# scale_percent = 80 # percent of original size
# width = int(image.shape[1] * scale_percent / 100)
# height = int(image.shape[0] * scale_percent / 100)
# image = processing.resize_image(image, width, height)

# data = detect.detection(image)

# image = processing.image_processing(image, data)
# # image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

# plt.imshow(image)
# plt.show()
