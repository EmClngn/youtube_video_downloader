# The vision is to create a youtube video downloader that is able to download videos and audio only
from pytube import YouTube


# pseudo code 

# follow the youtube video: https://youtu.be/vEQ8CXFWLZU?t=325
# adjust some things with the code in the yt video once have more knowledge about pytube
# idea is to combine the video with the downloaded audio but can't get ffmpeg to work
def video_downlaoder():
    video = yt.streams.get_highest_resolution()
    video.download(output_path=download_path)
    print("Video Download Complete")
# download video instead but for audio only
def audio_downlaoder():
    audio = yt.streams.filter(only_audio=True, mime_type = 'audio/mp4').first()
    audio.download(output_path=download_path)
    print("Audio Download Complete")


user_link = input("Paste here your desired Youtube link: ")
download_path = input("Paste here your desired download path: ")
options = input("Video or Audio?: ")
option_1 = "Video"
option_2 = "Audio"

yt = YouTube(user_link)
print("Title: ", yt.title)
print("View: ", yt.views)
if options == option_1:
    video_downlaoder()
elif options == option_2:
    audio_downlaoder()

# after all of that is done, make everything work with tkinter gui
