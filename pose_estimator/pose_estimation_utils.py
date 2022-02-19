from matplotlib.patches import Ellipse
import numpy as np
from consts import BODYPART_TO_IND


def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# TODO: make sure to handle the cases of missing body parts (including shoulders)
def get_location(keypoints_array, body_part):
    return keypoints_array[BODYPART_TO_IND[body_part]]


def get_head_ellipse(keypoints_array):
    # for readability. TODO: Change to OOP solution
    keypoints_map = {
        body_part: keypoints_array[BODYPART_TO_IND[body_part]] for body_part in BODYPART_TO_IND.keys()
    }

    center_point = np.mean([keypoints_map['left_ear'],
                            keypoints_map['right_ear']], axis=0)
    face_width = distance(keypoints_map['left_ear'], keypoints_map['right_ear'])

    # get chin's location
    chin_location = np.mean([keypoints_map['left_shoulder'],
                             keypoints_map['right_shoulder'],
                             keypoints_map['nose']],
                            axis=0)
    face_height = 2 * distance(keypoints_map['nose'], chin_location)
    # TODO: move drawing part to the drawing_utils file
    ellipse = Ellipse(xy=center_point, width=face_width, height=face_height,
                      fill=False, edgecolor='c', linewidth=3)
    return ellipse
