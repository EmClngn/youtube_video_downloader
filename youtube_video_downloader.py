# The vision is to create a youtube video downloader that is able to download videos and audio only
from pytube import YouTube
import subprocess

# pseudo code 

# follow the youtube video: https://youtu.be/vEQ8CXFWLZU?t=325
# adjust some things with the code in the yt video once have more knowledge about pytube
link = "https://youtu.be/jHjUHKdoaqI"
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

# idea is to combine the video with the downloaded audio but can't get ffmpeg to work
video = yt.streams.get_highest_resolution()

# download video instead but for audio only
audio = yt.streams.filter(only_audio=True, mime_type = 'audio/mp4').first()
audio.download(r'd:\youtube download')

# after all of that is done, make everything work with tkinter gui
