import yt_dlp
from youtubesearchpython import VideosSearch
from subprocess import run
from os import getlogin,makedirs,path
import sys

ascii_art2=r"""
██╗  ██╗███████╗███████╗██████╗ 
██║ ██╔╝██╔════╝██╔════╝██╔══██╗
█████╔╝ █████╗  █████╗  ██████╔╝
██╔═██╗ ██╔══╝  ██╔══╝  ██╔═══╝ 
██║  ██╗███████╗███████╗██║     
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     
                                
██╗     ██╗███████╗████████╗███████╗███╗   ██╗██╗███╗   ██╗ ██████╗    ██╗ 
██║     ██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║██║████╗  ██║██╔════╝ ██╗╚██╗
██║     ██║███████╗   ██║   █████╗  ██╔██╗ ██║██║██╔██╗ ██║██║  ███╗╚═╝ ██║
██║     ██║╚════██║   ██║   ██╔══╝  ██║╚██╗██║██║██║╚██╗██║██║   ██║██╗ ██║
███████╗██║███████║   ██║   ███████╗██║ ╚████║██║██║ ╚████║╚██████╔╝╚═╝██╔╝
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝ 
"""


print(ascii_art2)

if len(sys.argv)==1:
    name=input("Enter any song name you want to download: ")
else:
    name=""
    
    for ind,i in enumerate(sys.argv):
        if ind!=0:
            name+=" "+i

def download_ytvid_as_mp3(video_url,videoT):
    print("Downloading the audio....")
    try:
        makedirs(path.expanduser("~/Music/MySongs"))
    except:
        pass
    run(f"yt-dlp -x --audio-format mp3 -P '/home/{getlogin()}/Music/MySongs/' {video_url}", shell=True,capture_output=True)
    print("Done:)")


print("Searching....")
try:
    videosSearch = VideosSearch(name, limit = 1)
    vidURL=videosSearch.result()["result"][0]["link"]
    vidTitle=videosSearch.result()["result"][0]["title"]
    print("Downloading: ",vidTitle)

    download_ytvid_as_mp3(vidURL,vidTitle[:25].replace(" ",""))

except Exception as e:
    print("Error: ",e)
    print("Couldn't download, are you sure that you have an active internet connection?")

