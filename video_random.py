import os
import random
import sys
import moviepy
from datetime import datetime
from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

INPUT_PATH =r"C:\Users\micha\Desktop\input"
OUT_PATH = r"C:\Users\micha\Desktop"

def get_all_file_paths(directory, file_type):
  file_paths = []
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith(file_type):
        file_paths.append(os.path.join(root, file))
  return file_paths

def make_filename(d):
  date_str = d.strftime("%B_%y-%m-%d")
  filename = "VIDEO_BINGO_%s.mp4" % (date_str, )
  return os.path.join(OUT_PATH, filename)

if __name__ == '__main__':
  print("""
  o              o   __o__   o__ __o        o__ __o__/_   o__ __o            o__ __o    __o__   o          o        o__ __o           o__ __o      
 <|>            <|>    |    <|     v\      <|    v       /v     v\          <|     v\     |    <|\        <|>      /v     v\         /v     v\     
 < >            < >   / \   / \     <\     < >          />       <\         / \     <\   / \   / \\o      / \     />       <\       />       <\    
  \o            o/    \o/   \o/       \o    |         o/           \o       \o/     o/   \o/   \o/ v\     \o/   o/                o/           \o  
   v\          /v      |     |         |>   o__/_    <|             |>       |__  _<|     |     |   <\     |   <|       _\__o__  <|             |> 
    <\        />      < >   / \       //    |         \\           //        |       \   < >   / \    \o  / \   \\          |     \\           //  
      \o    o/         |    \o/      /     <o>          \         /         <o>      /    |    \o/     v\ \o/     \         /       \         /    
       v\  /v          o     |      o       |            o       o           |      o     o     |       <\ |       o       o         o       o     
        <\/>         __|>_  / \  __/>      / \  _\o__/_  <\__ __/>          / \  __/>   __|>_  / \        < \      <\__ __/>         <\__ __/>     
                                                                                                                                                  
""")

  imagefiles = []
  imagefiles = get_all_file_paths(INPUT_PATH, ".jpg")
  videofiles = []
  videofiles = get_all_file_paths(INPUT_PATH, ".mp4")
  videofiles = [file for file in videofiles if "begin.mp4" not in file and "end.mp4" not in file]

  if not videofiles:
    print("I couldn't find any video files :(")
    sys.exit(-1)

print("Found %d videos to shuffle" % (len(videofiles)))
print("Found %d images to shuffle" % (len(imagefiles)))

if len(imagefiles) != len(videofiles) and len(imagefiles) > 0:
  print("Found %d videos and %d images, image and video count must match if images present in input folder" % (len(videofiles),(len(imagefiles))))
  sys.exit(-2)

if len(imagefiles) == 0 and len(videofiles) > 0:
  random.shuffle(videofiles)

  for item in get_all_file_paths(INPUT_PATH, ".mp4"):
    if "begin.mp4" in item:
      print(item)
      videofiles.insert(0, item)

  for item in get_all_file_paths(INPUT_PATH, ".mp4"):
    if "end.mp4" in item:
      print(item)
      videofiles.insert(len(get_all_file_paths(INPUT_PATH, ".mp4")), item)

  video_file_list = []

  for i in videofiles:
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