import sys
import pandas as pd
import numpy as np
import cv2

from pose_estimator import pose_estimation, skeleton_creator
from video_processing import video_processor as vp
from outliers_handling import outliers_detector
from cloud_storage import cloud_manager
import moviepy.editor as mp

if __name__ == '__main__':
    # load resources for testing; will get from server
    video_path = sys.argv[1]
    bg_img_path = sys.argv[2] if len(sys.argv) > 2 else None

    # metadata extraction - width, height, fps, video length
    metadata = vp.get_metadata_for_video(video_path)

    # set black image as background if no background is given
    if bg_img_path is None:
        bg_img = np.zeros((metadata['width'], metadata['height'], 3))
    else:
        bg_img = cv2.imread(bg_img_path)
        bg_img = cv2.resize(bg_img, (metadata['height'], metadata['width']))

    # load data from cache in cloud
    pose_df = cloud_manager.load_pose_df(video_path)

    if pose_df is None:
        # video to images
        images_list = vp.video_to_images(video_path, save_to_disk=False)

        # pose estimation
        pose_df = pose_estimation.detect_pose(images_list)

        # TODO: Save results to cloud storage
        results_cache_success = cloud_manager.save_pose_df(pose_df, video_path)

    # when loading from csv, need to eval tuples
    else:
        pose_df = pose_df.astype(str).applymap(eval)

    # detect anomalies
    anomaly_inds = outliers_detector.detect_outliers(pose_df)

    # fix anomalies
    fixed_pose_df = outliers_detector.fix_outliers(pose_df, anomaly_inds)

    # draw generated images
    generated_images_list = skeleton_creator.generate_images(fixed_pose_df, mode='sticklight', background_image=bg_img,
                                                             colors_dict={('nose', 'left_eye'): (0, 0, 0),
                                                                          ('nose', 'right_eye'): (0, 0, 0),
                                                                          ('left_eye', 'left_ear'): (0, 0, 0),
                                                                          ('right_eye', 'right_ear'): (0, 0, 0),
                                                                          ('nose', 'left_shoulder'): (0, 0, 0),
                                                                          ('nose', 'right_shoulder'): (0, 0, 0)},
                                                             emoji_face='piggi')

    # create final video
    final_video_path = vp.images_to_video(generated_images_list, video_path, metadata=metadata, audio_source=video_path)

    # save video to cloud storage
    video_save_success = cloud_manager.save_video_to_cloud(final_video_path)
    # TODO: change this to "return" when not in "main"
    print(final_video_path)

#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys
# import split_and_merge.split_and_merge_videos as split_merge
# import os
# import tensorflow as tf
# import tensorflow_hub as hub
# import pose_estimator.sticklights_example as sticklight
# from pose_estimator.consts import *
# import matplotlib.pyplot as plt
#
#
# def manipulate_images(orig_images_path):
#     edited_images_dir = orig_images_path + "_edited"
#     os.mkdir(edited_images_dir)
#     # load model
#     module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
#     input_size = 192
#     model = module.signatures['serving_default']
#     # run over all directory
#     for file_path in os.listdir(orig_images_path):
#         try:
#             image_path = os.path.join(orig_images_path, file_path)
#             # run logic
#             image = tf.io.read_file(image_path)
#             # create pixel map
#             image = tf.image.decode_jpeg(image)
#
#             # select colors_dict
#             selected_colors_dict = {k: v for k, v in KEYPOINT_EDGE_INDS_TO_COLOR.items()}
#             selected_colors_dict.update({
#                 (14, 16): 'y'
#             })
#
#             # create sticklights image
#             sticklights_image = sticklight.draw_sticklights_image(image, model, input_size,  out_path=None, show_image=False,
#                                                                   colors_dict=selected_colors_dict)
#
#             # save edited image in edited_images_dir
#             out_path = os.path.join(edited_images_dir, file_path)
#             plt.imsave(out_path, sticklights_image)
#         except:
#             pass
#
#     return edited_images_dir
#
#
# if __name__ == '__main__':
#     # load video for testing; will get from server
#     video_path = sys.argv[1]
#
#     # video to images
#     images_list =
#
#
#     # for i in range(1, len(sys.argv)):
#     #     # TODO change args from path to video name
#     #     video_name = sys.argv[i]
#     #     # path = 'C:\\Users\\oritf\\PycharmProjects\\final_project\\hand'
#     #     pictures_dir_path = split_merge.video_to_picture(video_name)
#     #     # pictures_dir_path = "C:\\Users\\97254\\Documents\\CS\\ThirdYear\\final_project\\model_code\\outputs\\dance4"
#     #     # do the magic
#     #     edited_pictures_dir_path = manipulate_images(pictures_dir_path)
#     #     new_video_name, new_video_path = split_merge.pictures_to_video(edited_pictures_dir_path)
#     #     split_merge.compress_video(new_video_name, new_video_path)
#     #     print("DONE")
