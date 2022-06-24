import pandas as pd
import shutil
import datetime

from consts import *


def valid_file(file):
    return file.filename.endswith('.mp4')


def save_uploaded_file(file, video_name):
    if valid_file(file):
        # currentDT = datetime.datetime.now()
        # file_name = 'resources/videos/' + str(currentDT) + '.mp4'
        # file_name = file_name.replace(".", "").replace(" ", "").replace(":", "").replace("-", "")[:-3] + ".mp4"

        file_name = RESOURCES_DIR + VIDEOS_DIR + video_name
        file.save(file_name)
        return file_name
    else:
        raise TypeError("Uploaded file shoud be of type .mp4")


def save_pose_df(pose_df, video_path):
    try:
        pose_df.to_csv(RESOURCES_DIR + POSE_DFS_DIR + "".join(video_path.split("/")[-1].split(".")[:-1]) + "_pose_df.csv")
        return True
    except:
        return False


def load_pose_df(video_path):
    try:
        return pd.read_csv(RESOURCES_DIR + POSE_DFS_DIR + "".join(video_path.split("/")[-1].split(".")[:-1]) + "_pose_df.csv",
                           index_col=0)
    except:
        return None


def save_video_to_cloud(video_path):
    try:
        shutil.move(video_path, OUTPUTS_DIR + video_path)
        return True
    except:
        return False
