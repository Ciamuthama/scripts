from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
print("Video Title: ", yt.title)
yd = yt.streams.get_highest_resolution()
print("Downloading:", yt.title)
yd.download("D:\Download")