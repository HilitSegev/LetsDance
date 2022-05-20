import pandas as pd
from pose_estimator.consts import BODYPARTS, BONES, COLORS
import cv2


def plot_bone(bg_img, xs, ys, bone, selected_color):
    assert len(bone) == 2
    start_point = (xs.loc[bone[0]], ys.loc[bone[0]])
    end_point = (xs.loc[bone[1]], ys.loc[bone[1]])
    cv2.line(bg_img, start_point, end_point, color=selected_color, thickness=2)


def plot_skeleton(bg_img, xs, ys, colors_to_use):
    xs, ys = xs.apply(round), ys.apply(round)
    # plot bones
    for bone in BONES:
        plot_bone(bg_img, xs, ys, bone, selected_color=colors_to_use[bone])

    # plot nodes
    for center_coordinates in zip(xs, ys):
        cv2.circle(bg_img, center_coordinates, radius=1, color=(255, 0, 0), thickness=3)

    cv2.imwrite('test.png', bg_img)


def generate_images(fixed_pose_df, mode='sticklight', background_image=None, colors_dict=None):
    # save copy of original image
    orig_background_image = background_image.copy()

    colors_to_use = COLORS
    colors_to_use.update(colors_dict)

    final_images_list = []

    # load background_image
    height, width, channel = background_image.shape

    for i, v in fixed_pose_df.iterrows():
        background_image = orig_background_image.copy()

        xs, ys, scores = v.apply(lambda x: x[1]), v.apply(lambda x: x[0]), v.apply(lambda x: x[2])

        # change ratios of the skeleton to fit image shape
        xs *= width
        ys *= height

        # TODO: filter high scores only

        # add skeleton
        plot_skeleton(background_image, xs, ys, colors_to_use)

        # TODO: add emoji head

        # add final image to list of final images
        final_images_list.append(background_image)


    return final_images_list
