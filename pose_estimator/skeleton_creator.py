import pandas as pd
from pose_estimator.consts import BODYPARTS, BONES
import matplotlib.pyplot as plt


def plot_bone(v, bone):
    plt.plot([x[1] for x in v.loc[bone]], [x[0] for x in v.loc[bone]], linewidth=2, color='b')


def plot_skeleton(v):
    # plot nodes
    plt.scatter([x[1] for x in v.loc[BODYPARTS]], [x[0] for x in v.loc[BODYPARTS]], s=6)

    # plot bones
    for bone in BONES:
        plot_bone(v, list(bone))

    plt.gca().invert_yaxis()


def generate_images(fixed_pose_df, mode='sticklight', background_image=None):
    final_images_list = []
    # load background_image

    # change ratios of the skeleton to fit image shape

    for i, v in fixed_pose_df.iterrows():
        # "plot" image

        # add skeleton
        plot_skeleton(v)

        # TODO: add emoji head

        # add final image to list of final images

    return final_images_list