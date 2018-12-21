#mark002
from pytube import YouTube, Playlist
import logging
import threading
from threading import Thread

import sys

import os
import subprocess



logger = logging.getLogger(__name__)



import moviepy.editor as mp

def convertToMp3(name, directory):
    prefix = directory + "/" 
    oldName =  name + ".mp4"
    newName =  name + ".mp3"
    clip = mp.VideoFileClip(oldName).subclip(0,20)
    clip.audio.write_audiofile(newName)



class YoutubeDownloader:

    def __init__(self):
        self._fileName = None
        self._directory = None

    def run(self):
        self.downloadRoutine()

    #def convertToMp3(self):
    #    mp4 = "'%s'.mp4" % self._fileName
    #    mp3 = "'%s'.mp3" % self._fileName
    #    ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    #    subprocess.call(ffmpeg, shell=True)
    #    print("\nCOMPLETE MP3 CONVERSION\n")

    def downloadVideo(self,url, path):
        default_path = ""#'/home/skira/Downloads'
        if path is None:
            path = default_path
        self._directory = path

        yt = YouTube(url)
        fn = yt.title
        self._fileName = fn
            #name of Video
        thumbImg = yt.thumbnail_url
            #thumbnail img
        #print(yt.streams.all())
            #show all streams
        stream = yt.streams.first()
            #get the top stream of the video
        stream.download(path)
        print("Downloaded ",fn,' ','\n')

    def downloadPlaylist(self,url, path):
        pl = Playlist(url)
        pl.populate_video_urls()
        print ("List size is %s:" % len(pl.video_urls))
        pl.download_all(path)
        print("Downloaded list")

    def download(self,url, path, onlyAudio):
        default_path = ""
        if path is None:
            path = default_path
        self._directory = path
        print("Starting downloading")

        if 'list=' in url:
            self.downloadPlaylist(url, path)
        else:
            self.downloadVideo(url, path)
        if onlyAudio:
            convertToMp3(self._fileName, self._directory)

        print("Thank you for downloading ;P")

    def downloadRoutine(self):
        url = ""
        path = None
        if(len(sys.argv) > 1):
            url = sys.argv[1]
            #if len(sys.argv) > 2:
            #    path = sys.argv[2]
        
        onlyAudio = None

        while onlyAudio is None:        
            audio = input("Only Audio? (Y/n)")
            condYes = (audio == "Y") or (audio == "y")
            condNo = (audio == "N") or (audio == "n")
            if condYes:
                onlyAudio = True
                break
            elif condNo:
                onlyAudio = False               
                break
            else:
                continue

        while url is not None:
            url = input("Type in the URL: ")
            try:
                downloadThread = Thread(target=self.download, args=(url, path, onlyAudio))
                downloadThread.start()
            except Exception as e:
                logger.debug(e)
                print("LALALA", e)
                pass

if __name__ == "__main__":
    ytDown = YoutubeDownloader()
    ytDown.run()