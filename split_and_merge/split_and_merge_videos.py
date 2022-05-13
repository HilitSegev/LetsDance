import subprocess
import cv2
import os
import ffmpeg


def compress_video(video_name, video_path):
    my_path = os.getcwd()
    media_in = video_path + '\\' + video_name
    media_out = video_path + '\\compressed_' + video_name
    # subprocess.run('ffmpeg -i' + media_in.replace(" ", "\\ ") + '-vcodec libx264 -crf 22' + media_out.replace(" ", "\\ "))
    command = 'ffmpeg -i ' + media_in + ' -vcodec libx264 -crf 22 ' + media_out
    print(command)
    subprocess.run(command, shell=True)
    os.chdir(my_path)


def pictures_to_video(image_folder_path):
    text = image_folder_path.split('\\')
    new_video_name = 'new_' + text[-1] + '.avi'
    my_path = os.getcwd()
    new_video_path = my_path + '\\outputs'
    os.chdir(new_video_path)

    images = [img for img in os.listdir(image_folder_path) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder_path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(new_video_name, 0, 20, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder_path, image)))

    cv2.destroyAllWindows()
    video.release()
    os.chdir(my_path)
    return new_video_name, new_video_path
    # return image_folder_path
    # return video_name #TODO check the val - image_folder_path is ok?


# get path of the form- name.type
def create_dir(video_name):
    curr_path = os.getcwd()
    directory_path = curr_path + "\\outputs"
    text = video_name.split('.')
    directory_name = text[0]
    new_path = os.path.join(directory_path, directory_name)
    os.mkdir(new_path)  # TODO: fix case dir exist
    print("Directory '% s' created" % directory_name)
    return curr_path, new_path


def video_to_picture(video_name):
    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()
    count = 0
    pictures_path = ""
    my_path = ""
    text = video_name.split('\\')  # tmp code until changing args
    video_name = text[-1]  # tmp code until changing args
    if success:
        my_path, pictures_path = create_dir(video_name)
        os.chdir(pictures_path)

    while success:
        num = str(count).zfill(3)
        cv2.imwrite("frame" + num + ".jpg", image)  # save frame as JPG file
        success, image = vidcap.read()
        count += 1

    os.chdir(my_path)
    return pictures_path
