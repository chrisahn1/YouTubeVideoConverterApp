import tkinter
import tkinter.messagebox
import requests

import youtube_download

import database_file

db = database_file.ChannelDatabase
db.create_tables()


class MainGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.wm_title('YouTubeVideoConverterPlus')

        #LEFT SIDE SCROLLBAR
        self.firstFrame = tkinter.LabelFrame(self.main_window, text="YouTube Channels")
        self.firstFrame.grid(row=0, columnspan=10, sticky='NW', rowspan=10, padx=5, pady=5, ipadx=0, ipady=70)

        self.scrollbar1 = tkinter.Scrollbar(self.firstFrame)
        self.scrollbar1.pack(side="right", fill="y")

        self.channelList = tkinter.Listbox(self.firstFrame, yscrollcommand=self.scrollbar1.set)
        self.channelList.pack(side="left", fill="y")

        self.scrollbar1.config(command=self.channelList.yview)

        #RIGHT SIDE BUTTONS
        self.useChannels = tkinter.LabelFrame(self.main_window, text="Add/Delete/Settings/Download")
        self.useChannels.grid(row=0, column=15, columnspan=15, sticky='NW', rowspan=3, padx=5, pady=5,
                              ipadx=10, ipady=40)

        #Add Channel Button
        self.add_channel_btn = tkinter.Button(self.useChannels, text="Add Channel", command=self.add_channel)
        self.add_channel_btn.grid(row=2, column=0, sticky='W', padx=5, pady=2)


        #Delete Channel Button
        self.delete_channel_btn = tkinter.Button(self.useChannels, text="Delete Channel", command=self.delete_channel)
        self.delete_channel_btn.grid(row=4, column=0, padx=5, pady=2)


        #Settings Button
        self.settings_btn = tkinter.Button(self.useChannels, text="Settings", command=self.settings)
        self.settings_btn.grid(row=6, column=0, sticky='W', padx=5, pady=2)


        #Download Video Button
        self.download_vid_btn = tkinter.Button(self.useChannels, text="Download Video", command=self.download_vid)
        self.download_vid_btn.grid(row=8, column=0, sticky='W', padx=5, pady=2)

        tkinter.mainloop()






#**************************************************************************************
#
#*******************main_functions - First Page ***************************************
#
#**************************************************************************************
    def add_channel(self):
        self.root_add_channel = tkinter.Tk()
        self.root_add_channel.wm_title("Add Channel")

    def delete_channel(self):
        self.root_add_channel = tkinter.Tk()
        self.root_add_channel.wm_title("Delete Channel")

    def settings(self):
        self.root_settings = tkinter.Tk()
        self.root_settings.wm_title("Settings")

    def download_vid(self):
        self.root_download_vid = tkinter.Tk()
        self.root_download_vid.wm_title("Download Video")

        self.instruction_download_vid = tkinter.LabelFrame(self.root_download_vid, text='Downloading Video')
        self.instruction_download_vid.grid(row=0, columnspan=20, sticky='NW',
                                           rowspan=10, padx=5, pady=5, ipadx=10, ipady=4)

        self.label_name = tkinter.Label(self.instruction_download_vid, text='Enter URL of Video: ')
        self.label_name.grid(row=0, column=0)

        self.url_entry = tkinter.Entry(self.instruction_download_vid, width=20)
        self.url_entry.grid(row=0, column=2, sticky='W')

        self.download_button = tkinter.Button(self.instruction_download_vid, text='Download',
                                              command=self.downloading_vid)
        self.download_button.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        self.cancel_button = tkinter.Button(self.instruction_download_vid, text='Cancel',
                                            command=self.root_download_vid.destroy)
        self.cancel_button.grid(row=1, column=2, sticky='W', padx=5, pady=2)



#**************************************************************************************
#
#******************* download_vid button ***************************************
#
#**************************************************************************************

    def downloading_vid(self):
        self.root_downloading = tkinter.Tk()
        self.root_downloading.wm_title("Downloading...")

        self.vid_url = self.url_entry.get()

        youtube_download.Download(self.vid_url)

        self.url_display = tkinter.Label(self.root_downloading, text=self.vid_url)
        self.url_display.grid(row=0, column=0)







maingui = MainGUI()

