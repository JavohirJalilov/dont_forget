import cv2
import numpy as np
import matplotlib.pyplot as plt

color = (46, 204, 113) # emerald

def drawing_image(image,xmin,ymin,xmax,ymax,name):
    """
    Drawing image
    """
    start_point, end_point = (int(xmin),int(ymin)), (int(xmax),int(ymax))
    image = cv2.rectangle(
        image,
        start_point, 
        end_point,
        color=color,
        thickness = 2
        )

    text_size, _ = cv2.getTextSize(
        name,
        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
        fontScale=0.6,  
        thickness=1
        )
        
    text_w, text_h = text_size
    image = cv2.rectangle(
        image,
        (int(xmin),int(ymin)-text_h), 
        (int(xmin) + text_w, int(ymin)), 
        color=color, 
        thickness=-1
        )

    image = cv2.putText(
        image,
        name,
        org=(int(xmin),int(ymin)-5),
        fontFace=cv2.FONT_HERSHEY_DUPLEX, 
        fontScale=0.6, 
        color=(255, 255, 255), 
        thickness=1,
        lineType=cv2.FILLED
        )
        
    return image

def image_processing(image, data):
    """
    image processing for object detection
    """
    for xmin,ymin,xmax,ymax,confidence,label,name in data.values:
        area = abs(xmax-xmin)*abs(ymax-ymin)
        image = drawing_image(image, xmin,ymin,xmax,ymax,f"{name} {confidence:.2f}")
    return image

def resize_image(image, w,h):
    """
    Image resize with opencv
    """
    image = cv2.resize(image,(w, h))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image