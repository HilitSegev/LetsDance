import cv2


def video_to_images(video_path, save_to_disk=False):
    # init output
    if save_to_disk:
        out_path = video_path + "/temp/"
    else:
        frames_list = []

    # load frames
    vid_cap = cv2.VideoCapture(video_path)
    success, frame = vidcap.read()
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
