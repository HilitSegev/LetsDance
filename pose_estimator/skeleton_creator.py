import pandas as pd
from pose_estimator.consts import BODYPARTS, BONES
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as patches

def plot_bone(xs, ys, bone):
    plt.plot(xs.loc[bone], ys.loc[bone], linewidth=2, color='b')


def plot_skeleton(xs, ys):
    # plot nodes
    plt.scatter(xs, ys, s=6)

    # plot bones
    for bone in BONES:
        plot_bone(xs, ys, list(bone))

    plt.gca().invert_yaxis()


def generate_images(fixed_pose_df, mode='sticklight', background_image=None):
    final_images_list = []
    
    # load background_image
    height, width, channel = background_image.shape
    aspect_ratio = float(width) / height
    fig, ax = plt.subplots(figsize=(12 * aspect_ratio, 12))
    # To remove the huge white borders
    fig.tight_layout(pad=0)
    ax.margins(0)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.axis('off')

    im = ax.imshow(background_image)

    for i, v in fixed_pose_df.iterrows():
        xs, ys, scores = v.apply(lambda x: x[1]), v.apply(lambda x: x[0]), v.apply(lambda x: x[2])

        # change ratios of the skeleton to fit image shape
        xs *= background_image.shape[1]
        ys *= background_image.shape[0]

        # TODO: filter high scores only

        # add skeleton
        plot_skeleton(xs, ys)

        # TODO: add emoji head

        # add final image to list of final images
        final_images_list.append([ax])

        # remove skeleton from ax

    return final_images_list
