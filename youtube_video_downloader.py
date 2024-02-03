# The vision is to create a youtube video downloader that is able to download videos and audio only
from pytube import YouTube

# pseudo code 

# follow the youtube video: https://youtu.be/vEQ8CXFWLZU?t=325
# adjust some things with the code in the yt video once have more knowledge about pytube
link = "https://youtu.be/jHjUHKdoaqI"
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

video = yt.streams.filter(adaptive=True, mime_type='video/webm').first()
video.download(r'd:\youtube download')


# download video instead but for audio only
audio = yt.streams.filter(only_audio=True, mime_type = 'audio/mp4').first()
audio.download(r'd:\youtube download')

# error handling
# after all of that is done, make everything work with tkinter gui
