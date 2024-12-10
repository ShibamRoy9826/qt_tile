import yt_dlp
from youtubesearchpython import VideosSearch
from subprocess import run
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
    run(f"yt-dlp -x --audio-format mp3 -P '/home/shibam/Music/MySongs/' {video_url}", shell=True,capture_output=True)
    print("Done:)")


print("Searching....")
videosSearch = VideosSearch(name, limit = 1)
vidURL=videosSearch.result()["result"][0]["link"]
vidTitle=videosSearch.result()["result"][0]["title"]
print("Downloading: ",vidTitle)

download_ytvid_as_mp3(vidURL,vidTitle[:25].replace(" ",""))

