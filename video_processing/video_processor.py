import cv2
import os
import moviepy.editor as mp
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

AUDIO_FILE_NAME = r"audio_file.mp3"


def add_audio_to_video(video_file, audio_file):
    # load the video
    video_clip = VideoFileClip(video_file)
    # load the audio
    audio_clip = AudioFileClip(audio_file)

    final_clip = video_clip.set_audio(audio_clip)

    final_path = "final_" + video_file
    final_clip.write_videofile(final_path)
    return final_path


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


def images_to_video(generated_images_list, video_path, metadata, audio_source=None):
    # TODO: make video from images
    final_video_path = video_path.split("/")[-1]

    video = cv2.VideoWriter(final_video_path, cv2.VideoWriter_fourcc(*'MP4V'), metadata['fps'],
                            (metadata['height'], metadata['width']))

    for image in generated_images_list:
        video.write(image.astype('uint8'))

    cv2.destroyAllWindows()
    video.release()

    if audio_source is not None:
        my_clip = mp.VideoFileClip(audio_source)
        # TODO:is this the right place to put it?
        my_clip.audio.write_audiofile(AUDIO_FILE_NAME)
        # TODO: add audio to video
        final_video_path = add_audio_to_video(final_video_path, AUDIO_FILE_NAME)

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
