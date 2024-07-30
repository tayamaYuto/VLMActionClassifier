import cv2
import os
# import datetime
# import time
# from moviepy.editor import VideoFileClip, ImageSequenceClip

def video_to_image_all(input_path, output_path='./data/output', basename='f', extension='png',frame_num=10):
    """Save all frames of a video to images.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the images. Defaults to '../data/output'.
        basename (str, optional): basename for the saved images. Defaults to 'frame'.
        extension (str, optional): extension for the saved images. Defaults to 'jpg'.
        frame_num (int,optional): length of frame to procces. Defaults to .
    """
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        return


    #入力ファイルの拡張子を除いた名前を取得
    input_file_name = os.path.basename(input_path)
    input_file_name =os.path.splitext(input_file_name)[0]
    print(input_file_name)
    output_path = os.path.join(output_path, input_file_name)
    print(output_path)

    os.makedirs(output_path, exist_ok=True)



    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    digit = len(str(frame_count))


    n = 0
    while True:
        ret, frame = cap.read()
        if ret and n < frame_num:
            file_name = '{}_{}_{}.{}'.format(input_file_name, basename, str(n).zfill(digit), extension)
            full_path = os.path.join(output_path, file_name)
            cv2.imwrite(full_path, frame)
            n += 1

        elif  n > frame_num:
            break

        else:
            break