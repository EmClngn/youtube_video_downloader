# The vision is to create a youtube video downloader that is able to download videos and audio only
from pytube import YouTube

# pseudo code 

# follow the youtube video: https://youtu.be/vEQ8CXFWLZU?t=325
link = "https://youtu.be/i9SwzEhfBLc?si=O3lrZczmzTmQSEL7"
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('d:\youtube download')

# adjust some things with the code in the yt video once have more knowledge about pytube
# try to add a way to change video format into mp3 for music downloading
# error handling
# after all of that is done, make everything work with tkinter gui
