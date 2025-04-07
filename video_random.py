import os
import random
import sys
import moviepy
from datetime import datetime
#mg20250331
from moviepy import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


INPUT_PATH =r"C:\Users\micha\Desktop\input"
OUT_PATH = r"C:\Users\micha\Desktop"


def get_all_file_paths(directory):
  file_paths = []
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith(".mp4"):
        file_paths.append(os.path.join(root, file))
  return file_paths


def make_filename(d):
  date_str = d.strftime("%B_%y-%m-%d")
  filename = "VIDEO_BINGO_%s.mp4" % (date_str, )
  return os.path.join(OUT_PATH, filename)


if __name__ == '__main__':
  print("""
     ,--.  ,--.         ,--.  ,--.            
,--. ,--.`--' ,-| | ,---. ,---.   | |-. `--',--,--, ,---. ,---. 
\ `' / ,--.' .-. || .-. :| .-. |  | .-. ',--.|   \| .-. || .-. | 
 \  / | |\ `-' |\  --.' '-' '  | `-' || || || |' '-' '' '-' ' 
 `--'  `--' `---' `----' `---'   `---' `--'`--''--'.`- / `---' 
                             `---'     
""")
  input("this is a test")
  onlyfiles = []
  onlyfiles = get_all_file_paths(INPUT_PATH)

  if not onlyfiles:
    print("I couldn't find any video files :(")
    sys.exit(-1)

  print("Found %d videos to shuffle" % (len(onlyfiles)))

  random.shuffle(onlyfiles)
  video_file_list = []

  for i in onlyfiles:
    try:
      video_file_list.append(VideoFileClip(i))
    except:
      print("Couldn't load the video %s" % (i, ))
      print("Trying to continue and load the rest.")

  if not video_file_list:
    print("I couldn't load any videos at all :(")
    sys.exit(-2)

  final = concatenate_videoclips(video_file_list)

  today = datetime.today()
  dest_file = make_filename(today)
  print("Creating a jumbled video.")

  try:
    final.write_videofile(dest_file, audio_codec='aac')
  except:
    print("There was a problem creating the video file :(")
    raise

