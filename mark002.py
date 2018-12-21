#mark002
from pytube import YouTube, Playlist
import logging
import threading
from threading import Thread

import sys

logger = logging.getLogger(__name__)


class YoutubeDownloader:

    def __init__(self):
        pass
    def run(self):
        self.downloadRoutine()

    def downloadVideo(self,url, path):
        default_path = '/home/skira/Downloads'
        if path is None:
            path = default_path
        
        yt = YouTube(url)
        fn = yt.title
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

    def download(self,url,path):
        default_path = '/home/skira/Downloads'
        if path is None:
            path = default_path
        
        print("Starting downloading")

        if 'list=' in url:
            self.downloadPlaylist(url, path)
        else:
            self.downloadVideo(url, path)
        print("Thank you for downloading ;P")

    def downloadRoutine(self):
        url = ""
        path = None
        if(len(sys.argv) > 1):
            url = sys.argv[1]
            #if len(sys.argv) > 2:
            #    path = sys.argv[2]
        
        while url is not None:
            url = input("Type in the URL: ")
            try:
                downloadThread = Thread(target=self.download, args=(url, path))
                downloadThread.start()

            except Exception as e:
                logger.debug(e)
                print("LALALA", e)
                pass

if __name__ == "__main__":
    ytDown = YoutubeDownloader()
    ytDown.run()