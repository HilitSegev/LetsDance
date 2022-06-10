import pandas as pd
import numpy as np
from pose_estimator.consts import BODYPARTS, BONES, COLORS, FACE_POINTS
import cv2
from PIL import Image, ImageFont, ImageDraw
import emoji
from emojipy import Emoji


def plot_bone(bg_img, xs, ys, bone, selected_color):
    assert len(bone) == 2
    start_point = (xs.loc[bone[0]], ys.loc[bone[0]])
    end_point = (xs.loc[bone[1]], ys.loc[bone[1]])
    cv2.line(bg_img, start_point, end_point, color=selected_color, thickness=2)


def plot_skeleton(bg_img, xs, ys, colors_to_use, face_width, face_height, emoji_face):
    xs, ys = xs.apply(round), ys.apply(round)
    # plot bones
    for bone in BONES:
        if bone[0] in FACE_POINTS or bone[1] in FACE_POINTS:
            continue
        plot_bone(bg_img, xs, ys, bone, selected_color=colors_to_use[bone])

    # plot head
    if emoji_face is None:
        cv2.ellipse(bg_img, center=(xs.loc['face_center'], ys.loc['face_center']),
                    axes=(face_width // 2, face_height // 2),
                    angle=0,
                    startAngle=0,
                    endAngle=360,
                    color=(0, 0, 255),
                    thickness=2)
    else:
        emoji_img = cv2.imread('resources/emojis/' + emoji_face + '.png')
        max_dim = max(face_width, face_height)
        # make max_dim even to avoid size mismatch
        max_dim -= max_dim % 2
        resized_emoji_img = cv2.resize(emoji_img, (max_dim, max_dim))

        # use the original background
        bg_img_patch = bg_img[ys['face_center'] - (max_dim // 2):ys['face_center'] + (max_dim // 2),
                       xs['face_center'] - (max_dim // 2):xs['face_center'] + (max_dim // 2)]

        mask = np.all(resized_emoji_img == 0, axis=2)

        for i in range(3):
            bg_img_patch[:, :, i][~mask] = resized_emoji_img[:, :, i][~mask]

        bg_img[ys['face_center'] - (max_dim // 2):ys['face_center'] + (max_dim // 2),
        xs['face_center'] - (max_dim // 2):xs['face_center'] + (max_dim // 2)] = bg_img_patch

    # plot nodes, without face points
    for center_coordinates in zip(xs.drop(FACE_POINTS), ys.drop(FACE_POINTS)):
        cv2.circle(bg_img, center_coordinates, radius=1, color=(255, 0, 0), thickness=3)

    # cv2.imwrite('test.png', bg_img)


def generate_images(fixed_pose_df, mode='sticklight', background_image=None, colors_dict=None, emoji_face=None):
    # save copy of original image
    orig_background_image = background_image.copy()

    colors_to_use = COLORS
    colors_to_use.update(colors_dict)

    final_images_list = []

    # load background_image
    height, width, channel = background_image.shape

    for i, v in fixed_pose_df.iterrows():
        background_image = orig_background_image.copy()

        # get face dimensions and remove them from v
        face_width = int(v.loc['face_width'] * width)
        face_height = int(v.loc['face_height'] * height)

        v = v.drop(['face_width', 'face_height'])

        xs, ys, scores = v.apply(lambda x: x[1]), v.apply(lambda x: x[0]), v.apply(lambda x: x[2])

        # change ratios of the skeleton to fit image shape
        xs *= width
        ys *= height

        # TODO: filter high scores only

        # add skeleton
        plot_skeleton(background_image, xs, ys, colors_to_use, face_width, face_height, emoji_face)

        # TODO: add emoji head

        # add final image to list of final images
        final_images_list.append(background_image)

    return final_images_list
