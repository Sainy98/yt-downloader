
from pytube import YouTube
import pyfiglet
from termcolor import colored, cprint
txt = pyfiglet.figlet_format("Youtube Video Downloader")
print()
print(txt)
print("-created by Sainy")
print()
link = input("Enter Your Link: ")
print()
yt= YouTube(link)
print(yt.title)
print("=====================================================")
cprint("wait your video is loading.........","yellow")
stream= yt.streams.filter(progressive= "True",file_extension="mp4",mime_type="video/mp4")

video = list(enumerate(stream))

for i in video:
    print(i)
choice = int(input("enter your choice: "))
print()
print("Downloading.....")
stream[choice].download()
cprint("download successfully","green")














