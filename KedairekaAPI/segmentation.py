from PIL import Image
from io import BytesIO
import numpy as np
from os import path
from datetime import datetime
import pixellib
from pixellib.instance import custom_segmentation
import os
import glob

# def load_model():

# return model

# _model = load_model()

def get_current_datetime(str_format="%Y%m%d_%H%M%S") -> str:
    now = datetime.now()
    str_current_datetime = now.strftime(str_format)
    return str_current_datetime

def read_image (image_encoded):
    pil_image = Image.open(BytesIO(image_encoded.file.read()))
    file_name = get_current_datetime() + ".jpg"
    file_path = path.join("uploads", file_name)
    pil_image.save(file_path)
    return file_path




def instance_image(image:np.ndarray):
    segment_image = custom_segmentation()
    segment_image.inferConfig(num_classes= 1, class_names= ["BG", "Cephalopholis cyanostigma"])
    segment_image.load_model('D:\KedairekaAPI\models\cynostigma.h5')
    segmented = "D:\KedairekaAPI\segmented"
    segmask, output = segment_image.segmentImage(image, show_bboxes = True, output_image_name= (os.path.join(get_current_datetime() + "_segmented.jpg")))
    # output_image_name = output
    # print(type(output))
    # abc = cv2.imread(output)
    bounding_boxes = segmask['rois']
    new_bounding_boxes = [numpy_array.tolist() for numpy_array in bounding_boxes ]
    # print(type(new_bounding_boxes[0]))
    # print(type(output))
    class_ids = segmask['class_ids']
    new_class_ids = [numpy_array.tolist() for numpy_array in class_ids ]
    # return segment_image.segmentImage
    # print (new_bounding_boxes, new_class_ids)
    list_of_files = glob.glob(segmented + '/*')
    latest_file = max(list_of_files, key=os.path.getctime)    
    return {"bounding_boxes" : new_bounding_boxes, "class_ids" : new_class_ids, "image_url" : latest_file}