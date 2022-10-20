from pyexpat import model
import pixellib
# from pixellib.instance import instance_segmentation
from pixellib.instance import custom_segmentation

segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 1, class_names= ["BG", "Cephalopholis cyanostigma"])
segment_image.load_model('cynostigma.h5')

segment_image.segmentImage('variolaTestfix.jpg',show_bboxes = True, output_image_name="ikanout12.jpg")