import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub

from pose_estimator.consts import BODYPARTS

def detect_pose(images_list):
    # init pose_df
    pose_df = pd.DataFrame(index=range(len(images_list)), columns=BODYPARTS)

    # load pose detection model
    module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
    input_size = 192
    model = module.signatures['serving_default']

    # run over images
    for ind, image in enumerate(images_list):
        if ind % 100 == 0:
            print(f"{ind} / {len(images_list)}")

        # Resize and pad the image to keep the aspect ratio and fit the expected size.
        image = tf.expand_dims(image, axis=0)
        image = tf.image.resize_with_pad(image, input_size, input_size)

        # SavedModel format expects tensor type of int32.
        image = tf.cast(image, dtype=tf.int32)

        # Run model inference.
        outputs = model(image)

        # Output is a [1, 1, 17, 3] tensor.
        # TODO: Handle multiple images in one batch
        pose_df.loc[ind] = list(outputs['output_0'].numpy()[0, 0, :, :])

    return pose_df
