import pandas as pd
from pose_estimator.consts import BODYPARTS, BONES
import cv2


def plot_bone(bg_img, xs, ys, bone):
    assert len(bone) == 2
    start_point = (xs.loc[bone[0]], ys.loc[bone[0]])
    end_point = (xs.loc[bone[1]], ys.loc[bone[1]])
    cv2.line(bg_img, start_point, end_point, color=(0, 255, 0), thickness=2)


def plot_skeleton(bg_img, xs, ys):
    xs, ys = xs.apply(round), ys.apply(round)
    # plot nodes
    for center_coordinates in zip(xs, ys):
        cv2.circle(bg_img, center_coordinates, radius=1, color=(255, 0, 0), thickness=3)

    for bone in BONES:
        plot_bone(bg_img, xs, ys, list(bone))

    cv2.imwrite('test.png', bg_img)


def generate_images(fixed_pose_df, mode='sticklight', background_image=None):
    final_images_list = []

    # load background_image
    height, width, channel = background_image.shape

    for i, v in fixed_pose_df.iterrows():
        xs, ys, scores = v.apply(lambda x: x[1]), v.apply(lambda x: x[0]), v.apply(lambda x: x[2])

        # change ratios of the skeleton to fit image shape
        xs *= width
        ys *= height

        # TODO: filter high scores only

        # add skeleton
        plot_skeleton(background_image, xs, ys)

        # TODO: add emoji head

        # add final image to list of final images
        final_images_list.append([ax])

        # remove skeleton from ax

    return final_images_list
