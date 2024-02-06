# The vision is to create a youtube video downloader that is able to download videos and audio only
from pytube import YouTube

# pseudo code 

# follow the youtube video: https://youtu.be/vEQ8CXFWLZU?t=325
# adjust some things with the code in the yt video once have more knowledge about pytube
# idea is to combine the video with the downloaded audio but can't get ffmpeg to work
def video_downlaoder():
    try:
        user_link = input("Paste here your desired Youtube link: ")
        download_path = input("Paste here your desired download path: ")
        yt = YouTube(user_link)
        print("Title: ", yt.title)
        print("View: ", yt.views)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=download_path)
        print("Video Download Complete")
    except Exception as e:
        print("An error occured:", str(e))
# download video instead but for audio only
def audio_downlaoder():
    try:
        user_link = input("Paste here your desired Youtube link: ")
        download_path = input("Paste here your desired download path: ")
        yt = YouTube(user_link)
        print("Title: ", yt.title)
        print("View: ", yt.views)
        audio = yt.streams.filter(only_audio=True, mime_type = 'audio/mp4').first()
        audio.download(output_path=download_path)
        print("Audio Download Complete")
    except Exception as e:
        print("An error occured:", str(e))



options = input("Press '0' if you want Video or press '1' if you want Audio: ")
option_1 = "0"
option_2 = "1"
if options == option_1:
    video_downlaoder()
elif options == option_2:
    audio_downlaoder()


