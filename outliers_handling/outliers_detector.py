def detect_outliers(pose_df):
    # TODO: Detect outliers, return list of anomaly_inds
    return []


def fix_outliers(pose_df, anomaly_inds):
    # TODO: Fix outliers
    if len(anomaly_inds) == 0:
        # smooth
        pose_df[['face_width', 'face_height']] = pose_df[['face_width', 'face_height']].rolling(50).mean().fillna(
            method='bfill')
    return pose_df
