import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub

from pose_estimator.consts import BODYPARTS
import numpy as np


def detect_pose(images_list):
    def distance(p1, p2):
        p1, p2 = np.asarray(p1), np.asarray(p2)
        return np.linalg.norm(p1 - p2)

    def tuple_mean(tuple_of_tuples):
        return tuple(
            sum([t[i] for t in tuple_of_tuples]) / len(tuple_of_tuples) \
            for i in range(len(tuple_of_tuples[0]))
        )

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
        body_poses = [tuple(x) for x in list(outputs['output_0'].numpy()[0, 0, :, :])]
        pose_df.loc[ind] = body_poses + [0]*(len(pose_df.loc[ind]) - len(body_poses))

        # detect face
        # using [1,2,3] to allow assignment of tuple to cell in DataFrame
        pose_df.loc[ind, [1, 2, 3]] = tuple_mean((pose_df.loc[ind, 'left_ear'], pose_df.loc[ind, 'right_ear']))
        pose_df.loc[[ind], 'face_center'] = pose_df.loc[[ind], [1, 2, 3]].apply(tuple, axis=1)
        pose_df.loc[ind, 'face_width'] = distance(pose_df.loc[ind, 'left_ear'][:-1], pose_df.loc[ind, 'right_ear'][:-1])

        pose_df.loc[ind, [1, 2, 3]] = tuple_mean((pose_df.loc[ind, 'left_shoulder'],
                                                  pose_df.loc[ind, 'right_shoulder'],
                                                  pose_df.loc[ind, 'nose']))
        pose_df.loc[[ind], 'chin'] = pose_df.loc[[ind], [1, 2, 3]].apply(tuple, axis=1)
        pose_df.loc[ind, 'face_height'] = 2 * distance(pose_df.loc[ind, 'nose'][:-1], pose_df.loc[ind, 'chin'][:-1])

        # remove temp columns
        pose_df.drop([1, 2, 3], axis=1, inplace=True)

    return pose_df
