import os
import random
import sys

from datetime import datetime
from moviepy.editor import ImageClip
from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg"):
                file_paths.append(os.path.join(root, file))
    return file_paths


images_path = r"C:\Users\micha\Desktop\input"

images_ = get_all_file_paths(images_path)

for i in images_:
    print(i)
    final = ImageClip(i)
    final = final.set_duration(100)
    final.write_videofile(r"C:\Users\micha\Desktop\input\images_video\i.mp4",fps=24)


