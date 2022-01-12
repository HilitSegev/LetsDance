import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import sys
import matplotlib.pyplot as plt

import drawing_utils
from consts import *


def detect_pose(input_image, model):
    """Runs detection on an input image.

    Args:
      input_image: A [1, height, width, 3] tensor represents the input image
        pixels. Note that the height/width should already be resized and match the
        expected input resolution of the model before passing into this function.

    Returns:
      A [1, 1, 17, 3] float numpy array representing the predicted keypoint
      coordinates and scores.
    """
    # Resize and pad the image to keep the aspect ratio and fit the expected size.
    input_image = tf.expand_dims(input_image, axis=0)
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

    # SavedModel format expects tensor type of int32.
    input_image = tf.cast(input_image, dtype=tf.int32)
    # Run model inference.
    outputs = model(input_image)
    # Output is a [1, 1, 17, 3] tensor.
    # TODO: check exactly what "outputs" is
    keypoints_with_scores = outputs['output_0'].numpy()
    return keypoints_with_scores


def draw_sticklights_image(input_image, model, out_path=None, show_image=False,
                           colors_dict=KEYPOINT_EDGE_INDS_TO_COLOR):
    # create black image, the same size as "input_image"
    black_image = np.zeros(input_image.shape)

    # run model for the input image and extract the keypoints_with_scores
    keypoints_with_scores = detect_pose(input_image, model)

    # use "drawing_utils" to plot the keypoints_with_scores on the black image
    sticklights_image = drawing_utils.draw_prediction_on_image(black_image, keypoints_with_scores,
                                                               colors_dict=colors_dict)

    # show and save
    if out_path is not None:
        plt.imsave(out_path, sticklights_image)
    if show_image:
        plt.imshow(sticklights_image)
        plt.show()

    return sticklights_image


if __name__ == "__main__":
    # parse parameters
    input_image, out_path = sys.argv[1:]

    # load model - lightning
    module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
    input_size = 192
    model = module.signatures['serving_default']

    # # load model - thunder
    # module = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
    # input_size = 256
    # model = module.signatures['serving_default']

    # load image
    image_path = sys.argv[1]
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image)

    # select colors_dict
    selected_colors_dict = {k: v for k, v in KEYPOINT_EDGE_INDS_TO_COLOR.items()}
    selected_colors_dict.update({
        (14, 16): 'y'
    })

    # create sticklights image
    sticklights_image = draw_sticklights_image(image, model, out_path, show_image=False,
                                               colors_dict=selected_colors_dict)
