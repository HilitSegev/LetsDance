# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import split_and_merge.split_and_merge_videos as split_merge


if __name__ == '__main__':

    for i in range(1, len(sys.argv)):
        #TODO change args from path to video name
        video_name = sys.argv[i]
        # path = 'C:\\Users\\oritf\\PycharmProjects\\final_project\\hand'
        pictures_dir_path = split_merge.video_to_picture(video_name)
        new_video_name, new_video_path = split_merge.pictures_to_video(pictures_dir_path)
        split_merge.compress_video(new_video_name, new_video_path)