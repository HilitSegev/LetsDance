BODYPARTS = ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear', 'left_shoulder', 'right_shoulder', 'left_elbow',
             'right_elbow', 'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
             'left_ankle', 'right_ankle']

BONES = [('nose', 'left_eye'),
         ('nose', 'right_eye'),
         ('left_eye', 'left_ear'),
         ('right_eye', 'right_ear'),
         ('nose', 'left_shoulder'),
         ('nose', 'right_shoulder'),
         ('left_shoulder', 'left_elbow'),
         ('left_elbow', 'left_wrist'),
         ('right_shoulder', 'right_elbow'),
         ('right_elbow', 'right_wrist'),
         ('left_shoulder', 'right_shoulder'),
         ('left_shoulder', 'left_hip'),
         ('right_shoulder', 'right_hip'),
         ('left_hip', 'right_hip'),
         ('left_hip', 'left_knee'),
         ('left_knee', 'left_ankle'),
         ('right_hip', 'right_knee'),
         ('right_knee', 'right_ankle')]

COLORS = {('nose', 'left_eye'): (0, 255, 0),
          ('nose', 'right_eye'): (0, 255, 0),
          ('left_eye', 'left_ear'): (0, 255, 0),
          ('right_eye', 'right_ear'): (0, 255, 0),
          ('nose', 'left_shoulder'): (0, 255, 0),
          ('nose', 'right_shoulder'): (0, 255, 0),
          ('left_shoulder', 'left_elbow'): (0, 255, 0),
          ('left_elbow', 'left_wrist'): (0, 255, 0),
          ('right_shoulder', 'right_elbow'): (0, 255, 0),
          ('right_elbow', 'right_wrist'): (0, 255, 0),
          ('left_shoulder', 'right_shoulder'): (0, 255, 0),
          ('left_shoulder', 'left_hip'): (0, 255, 0),
          ('right_shoulder', 'right_hip'): (0, 255, 0),
          ('left_hip', 'right_hip'): (0, 255, 0),
          ('left_hip', 'left_knee'): (0, 255, 0),
          ('left_knee', 'left_ankle'): (0, 255, 0),
          ('right_hip', 'right_knee'): (0, 255, 0),
          ('right_knee', 'right_ankle'): (0, 255, 0)}

# Dictionary that maps from joint names to keypoint indices.
BODYPART_TO_IND = {
    'nose': 0,
    'left_eye': 1,
    'right_eye': 2,
    'left_ear': 3,
    'right_ear': 4,
    'left_shoulder': 5,
    'right_shoulder': 6,
    'left_elbow': 7,
    'right_elbow': 8,
    'left_wrist': 9,
    'right_wrist': 10,
    'left_hip': 11,
    'right_hip': 12,
    'left_knee': 13,
    'right_knee': 14,
    'left_ankle': 15,
    'right_ankle': 16
}

IND_TO_BODYPART = {v: k for k, v in BODYPART_TO_IND.items()}

# Maps bones to a matplotlib color name.
KEYPOINT_EDGE_INDS_TO_COLOR = {
    (0, 1): 'k',
    (0, 2): 'k',
    (1, 3): 'k',
    (2, 4): 'k',
    (0, 5): 'k',
    (0, 6): 'k',
    (5, 7): 'm',
    (7, 9): 'm',
    (6, 8): 'c',
    (8, 10): 'c',
    (5, 6): 'y',
    (5, 11): 'm',
    (6, 12): 'c',
    (11, 12): 'y',
    (11, 13): 'm',
    (13, 15): 'm',
    (12, 14): 'c',
    (14, 16): 'c'
}

KEYPOINT_EDGE_BODYPARTS_TO_COLOR = {
    (IND_TO_BODYPART[k[0]], IND_TO_BODYPART[k[1]]): v for k, v in KEYPOINT_EDGE_INDS_TO_COLOR.items()
}
