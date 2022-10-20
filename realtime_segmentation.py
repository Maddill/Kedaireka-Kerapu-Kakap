from email.mime import image
from tkinter import Frame
from unittest import result
import cv2
import pixellib
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")
cam = cv2.VideoCapture(0)

while cam.isOpened():
    res, Frame= cam.read()
    ##Apply Segementation
    result=segment_image.segmentFrame(Frame,show_bboxes=True)
    image=result[1]
    cv2.imshow('Image segmentation', image)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()