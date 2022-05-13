# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import split_and_merge.split_and_merge_videos as split_merge
import os
import tensorflow as tf
import tensorflow_hub as hub
import pose_estimator.sticklights_example as sticklight
from pose_estimator.consts import *
import matplotlib.pyplot as plt


def manipulate_images(orig_images_path):
    edited_images_dir = orig_images_path + "_edited"
    os.mkdir(edited_images_dir)
    # load model
    module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
    input_size = 192
    model = module.signatures['serving_default']
    # run over all directory
    for file_path in os.listdir(orig_images_path):
        try:
            image_path = os.path.join(orig_images_path, file_path)
            # run logic
            image = tf.io.read_file(image_path)
            # create pixel map
            image = tf.image.decode_jpeg(image)

            # select colors_dict
            selected_colors_dict = {k: v for k, v in KEYPOINT_EDGE_INDS_TO_COLOR.items()}
            selected_colors_dict.update({
                (14, 16): 'y'
            })

            # create sticklights image
            sticklights_image = sticklight.draw_sticklights_image(image, model, input_size,  out_path=None, show_image=False,
                                                                  colors_dict=selected_colors_dict)

            # save edited image in edited_images_dir
            out_path = os.path.join(edited_images_dir, file_path)
            plt.imsave(out_path, sticklights_image)
        except:
            pass

    return edited_images_dir


if __name__ == '__main__':

    for i in range(1, len(sys.argv)):
        # TODO change args from path to video name
        video_name = sys.argv[i]
        # path = 'C:\\Users\\oritf\\PycharmProjects\\final_project\\hand'
        pictures_dir_path = split_merge.video_to_picture(video_name)
        # pictures_dir_path = "C:\\Users\\97254\\Documents\\CS\\ThirdYear\\final_project\\model_code\\outputs\\dance4"
        # do the magic
        edited_pictures_dir_path = manipulate_images(pictures_dir_path)
        new_video_name, new_video_path = split_merge.pictures_to_video(edited_pictures_dir_path)
        split_merge.compress_video(new_video_name, new_video_path)
        print("DONE")
