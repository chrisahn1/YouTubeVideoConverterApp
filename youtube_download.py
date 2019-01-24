import pytube
import tkinter
import tkinter as tk
import threading

import getpass

from tkinter import ttk


class Download:
    def __init__(self, vid_url):
        # self.path = f'https://www.youtube.com/watch?v=lZAB3_KAu1A'
        # self.path = f'{vid_url}'
        self.root_downloading = tk.Tk()


        self.path = vid_url

        username = getpass.getuser()

        self.FolderLocation = "C:/Users/{}/Downloads/".format(username)

        # self.yt = pytube.YouTube(self.path, on_progress_callback=self.progress_function)

        self.yt = pytube.YouTube(self.path)

        # video_type = self.yt.streams.filter(file_extension='mp4').first()
        #
        # self.MaxFileSize = video_type.filesize


        #**************************************************************************************************
        # Loading label
        # self.loadingLabel = ttk.Label(self.root_downloading, text="Loading...", font=("Agency FB", 30))
        # self.loadingLabel.grid(pady=(100, 0))
        #
        # # loading precent label which must show % donwloaded
        # self.loadingPercent = tk.Label(self.root_downloading, text="0", fg="green", font=("Agency FB", 30))
        # self.loadingPercent.grid(pady=(30, 30))
        #
        # # indeterminate progress bar
        # self.progressbar = ttk.Progressbar(self.root_downloading, orient="horizontal", length=500, mode='indeterminate')
        # self.progressbar.grid(pady=(50, 0))
        # self.progressbar.start()


        # threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress_bar(self.MaxFileSize))).start()
        #
        # # call Download file func
        # threading.Thread(target=self.DownloadFile(self.FolderLocation)).start()
        #*****************************************************************************************************

        # bytes_remaining = 0
        # self.loadingPercent.config(text=str(int(100 - (100 * (bytes_remaining / self.MaxFileSize)))))

        self.stream = self.yt.streams.first()
        self.stream.download(self.FolderLocation)













# path = f'https://www.youtube.com/watch?v=lZAB3_KAu1A'
# yt = pytube.YouTube(path)
# stream = yt.streams.first()
# stream.download()