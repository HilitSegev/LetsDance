import pandas as pd


def save_pose_df(pose_df, video_path):
    try:
        pose_df.to_csv("resources/pose_dfs/" + "".join(video_path.split("/")[-1].split(".")[:-1]) + "_pose_df.csv")
        return True
    except:
        return False


def load_pose_df(video_path):
    try:
        return pd.read_csv("resources/pose_dfs/" + "".join(video_path.split("/")[-1].split(".")[:-1]) + "_pose_df.csv",
                           index_col=0)
    except:
        return None
