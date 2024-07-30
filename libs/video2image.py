import argparse
import os
from video2image_func import video_to_image_all


#実行コード
# python video2image.py ../data/input/img_3822.mov  
print(os.getcwd())

parser = argparse.ArgumentParser(description='Save all frames of a video to images.')
parser.add_argument('input_path', type=str,help='Path to the input video folder.')
parser.add_argument('-o','--output_path', type=str, default="../data/output",  help='Directory to save the images. Defaoult is "../data/output"')
parser.add_argument('-b', '--basename', type=str, default='f', help='Basename for the saved images. Default is "f".')
parser.add_argument('-ie', '--img_extension', type=str, default='png', help='img_extension for the saved images. Default is "png".')
parser.add_argument('-fn', '--frame_num', type=int, default=10, help='length of frame to process')

args = parser.parse_args()

#入力フォルダからファイル名を取得
file_path = args.input_path

video_to_image_all(file_path, args.output_path, args.basename, args.img_extension, args.frame_num)
