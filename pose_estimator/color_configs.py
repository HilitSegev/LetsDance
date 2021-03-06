COLORS = {'green': {'head': (0, 255, 0),
                    ('nose', 'left_eye'): (0, 255, 0),
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
                    ('right_knee', 'right_ankle'): (0, 255, 0)},
          'light_blue': {('nose', 'left_eye'): (38, 255, 255),
                         ('nose', 'right_eye'): (38, 255, 255),
                         ('left_eye', 'left_ear'): (38, 255, 255),
                         ('right_eye', 'right_ear'): (38, 255, 255),
                         ('nose', 'left_shoulder'): (38, 255, 255),
                         ('nose', 'right_shoulder'): (38, 255, 255),
                         ('left_shoulder', 'left_elbow'): (38, 255, 255),
                         ('left_elbow', 'left_wrist'): (38, 255, 255),
                         ('right_shoulder', 'right_elbow'): (38, 255, 255),
                         ('right_elbow', 'right_wrist'): (38, 255, 255),
                         ('left_shoulder', 'right_shoulder'): (38, 255, 255),
                         ('left_shoulder', 'left_hip'): (38, 255, 255),
                         ('right_shoulder', 'right_hip'): (38, 255, 255),
                         ('left_hip', 'right_hip'): (38, 255, 255),
                         ('left_hip', 'left_knee'): (38, 255, 255),
                         ('left_knee', 'left_ankle'): (38, 255, 255),
                         ('right_hip', 'right_knee'): (38, 255, 255),
                         ('right_knee', 'right_ankle'): (38, 255, 255)},
          'pink_light_blue_yellow': {'head': (255, 61, 246),
                                     ('nose', 'left_eye'): (0, 255, 0),
                                     ('nose', 'right_eye'): (0, 255, 0),
                                     ('left_eye', 'left_ear'): (0, 255, 0),
                                     ('right_eye', 'right_ear'): (0, 255, 0),
                                     ('nose', 'left_shoulder'): (0, 255, 0),
                                     ('nose', 'right_shoulder'): (0, 255, 0),
                                     ('left_shoulder', 'left_elbow'): (255, 61, 246),
                                     ('left_elbow', 'left_wrist'): (255, 61, 246),
                                     ('right_shoulder', 'right_elbow'): (38, 255, 255),
                                     ('right_elbow', 'right_wrist'): (38, 255, 255),
                                     ('left_shoulder', 'right_shoulder'): (255, 233, 114),
                                     ('left_shoulder', 'left_hip'): (255, 61, 246),
                                     ('right_shoulder', 'right_hip'): (38, 255, 255),
                                     ('left_hip', 'right_hip'): (255, 233, 114),
                                     ('left_hip', 'left_knee'): (38, 255, 255),
                                     ('left_knee', 'left_ankle'): (38, 255, 255),
                                     ('right_hip', 'right_knee'): (255, 61, 246),
                                     ('right_knee', 'right_ankle'): (255, 61, 246)},
          'purple_pink_yellow': {'head': (255, 120, 12),
                                 ('nose', 'left_eye'): (0, 255, 0),
                                 ('nose', 'right_eye'): (0, 255, 0),
                                 ('left_eye', 'left_ear'): (0, 255, 0),
                                 ('right_eye', 'right_ear'): (0, 255, 0),
                                 ('nose', 'left_shoulder'): (0, 255, 0),
                                 ('nose', 'right_shoulder'): (0, 255, 0),
                                 ('left_shoulder', 'left_elbow'): (255, 120, 12),
                                 ('left_elbow', 'left_wrist'): (255, 120, 12),
                                 ('right_shoulder', 'right_elbow'): (255, 14, 150),
                                 ('right_elbow', 'right_wrist'): (255, 14, 150),
                                 ('left_shoulder', 'right_shoulder'): (255, 232, 10),
                                 ('left_shoulder', 'left_hip'): (255, 120, 12),
                                 ('right_shoulder', 'right_hip'): (255, 14, 150),
                                 ('left_hip', 'right_hip'): (255, 232, 10),
                                 ('left_hip', 'left_knee'): (255, 120, 12),
                                 ('left_knee', 'left_ankle'): (255, 120, 12),
                                 ('right_hip', 'right_knee'): (255, 14, 150),
                                 ('right_knee', 'right_ankle'): (255, 14, 150)},
          'green_purple': {'head': (190, 42, 255),
                           ('nose', 'left_eye'): (0, 255, 0),
                           ('nose', 'right_eye'): (0, 255, 0),
                           ('left_eye', 'left_ear'): (0, 255, 0),
                           ('right_eye', 'right_ear'): (0, 255, 0),
                           ('nose', 'left_shoulder'): (0, 255, 0),
                           ('nose', 'right_shoulder'): (0, 255, 0),
                           ('left_shoulder', 'left_elbow'): (190, 42, 255),
                           ('left_elbow', 'left_wrist'): (190, 42, 255),
                           ('right_shoulder', 'right_elbow'): (36, 255, 76),
                           ('right_elbow', 'right_wrist'): (36, 255, 76),
                           ('left_shoulder', 'right_shoulder'): (0, 0, 255),
                           ('left_shoulder', 'left_hip'): (190, 42, 255),
                           ('right_shoulder', 'right_hip'): (36, 255, 76),
                           ('left_hip', 'right_hip'): (0, 0, 255),
                           ('left_hip', 'left_knee'): (190, 42, 255),
                           ('left_knee', 'left_ankle'): (190, 42, 255),
                           ('right_hip', 'right_knee'): (36, 255, 76),
                           ('right_knee', 'right_ankle'): (36, 255, 76)}
          }
