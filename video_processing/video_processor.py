import cv2
import os
import moviepy.editor as mp


def video_to_images(video_path, save_to_disk=False):
    # init output
    if save_to_disk:
        out_path = "".join(video_path.split(".")[:-1]) + "_temp/"
        if not os.path.exists(out_path):
            os.mkdir(out_path)
    else:
        frames_list = []

    # load frames
    vid_cap = cv2.VideoCapture(video_path)
    success, frame = vid_cap.read()
    counter = 0
    while success:
        if save_to_disk:
            # save frame as JPEG file
            cv2.imwrite(out_path + "frame%d.jpg" % counter, frame)
            counter += 1
        else:
            # add to frames list
            frames_list.append(frame)
        success, frame = vid_cap.read()

    # return
    return out_path if save_to_disk else frames_list


def images_to_video(generated_images_list, video_path, audio_source=None):
    # TODO: make video from images
    final_video_path = ...

    if audio_source is not None:
        my_clip = mp.VideoFileClip(video_path)
        #TODO:is this the right place to put it?
        my_clip.audio.write_audiofile(r"audio_file.mp3")
        #TODO: add audio to video
        final_video_path = add_audio_to_video(final_video_path,audio_file)

    return final_video_path


def get_metadata_for_video(video_path):
    vid_cap = cv2.VideoCapture(video_path)
    metadata = dict()
    if vid_cap.isOpened():
        metadata['width'] = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        metadata['height'] = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        metadata['fps'] = int(vid_cap.get(cv2.CAP_PROP_FPS))
        metadata['total_frames'] = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return metadata