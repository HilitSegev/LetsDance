import pandas as pd
import numpy as np


def detect_outliers(pose_df):
    # Detect outliers, return list of anomaly_inds
    df = pose_df.select_dtypes(exclude=[np.number])
    xs, ys, scores = (df.applymap(lambda x: x[i]) for i in [1, 0, 2])
    # first condition: at least 50% of the bodyparts with score higher than 0.3
    cond1_series = (scores.median(axis=1) < 0.3)

    # second condition: face_center must be higher than both shoulders
    cond2_series = (ys['face_center'] > ys['left_shoulder']) & (ys['face_center'] > ys['right_shoulder'])

    # return anomalies of they satisfy at least one condition
    return df.loc[cond1_series | cond2_series].index


def tuple_smoothing(s, window=5):
    """
    s is a series of tuples
    """

    def series_smoothing(s, window=5):
        return s.rolling(window).mean().fillna(method='bfill')

    xs, ys, scores = series_smoothing(s.apply(lambda x: x[1]), window), \
                     series_smoothing(s.apply(lambda x: x[0]), window), \
                     series_smoothing(s.apply(lambda x: x[2]), window)

    smoothed_s = pd.Series(list(pd.DataFrame().assign(y=ys, x=xs, score=scores).to_records(index=False)))
    return smoothed_s


def fix_outliers(pose_df, anomaly_inds):
    # TODO: Fix outliers and remove from anomaly_inds
    df = pose_df.select_dtypes(exclude=[np.number])
    xs, ys, scores = (df.applymap(lambda x: x[i]) for i in [1, 0, 2])

    anom_start = 0
    anom_end = 0
    i = 0
    while i < df.shape[0]:
        if i in anomaly_inds:
            anom_start = i
            while i in anomaly_inds:
                i += 1
            anom_end = i - 1

            # interpolate
            anom_len = anom_end - anom_start + 1
            int_x = np.linspace(xs.iloc[anom_start - 1], xs.iloc[anom_end + 1], anom_len + 2)
            int_y = np.linspace(ys.iloc[anom_start - 1], ys.iloc[anom_end + 1], anom_len + 2)
            int_score = np.linspace(scores.iloc[anom_start - 1], scores.iloc[anom_end + 1], anom_len + 2)

            # make interpolation df
            int_df = pd.concat([
                pd.Series(list(
                    pd.DataFrame()
                        .assign(y=int_y[:, k], x=int_x[:, k], score=int_score[:, k])
                        .to_records(index=False)))
                for k in range(int_x.shape[1])
            ], axis=1)
            int_df.index = range(anom_start - 1, anom_end + 2)
            int_df.columns = df.columns

            pose_df.loc[int_df.index, int_df.columns] = int_df
            i+=1
        else:
            i += 1

    # smooth the face location
    pose_df[['face_width', 'face_height']] = (
        pose_df[['face_width', 'face_height']]
            .rolling(50)
            .median()
            .fillna(method='bfill')
    )

    # smooth the bodyparts
    for bodypart in pose_df.columns:
        if bodypart in ['face_width', 'face_height']:
            continue
        pose_df[bodypart] = tuple_smoothing(pose_df[bodypart], window=5)

    return pose_df
