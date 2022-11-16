from tkinter import *
import customtkinter
import subprocess
import os
from pathlib import Path
# import filedialog module
from tkinter import filedialog


class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 600
    FILE_TO_SEND = ''
    FILE_TO_GET = ''
    DEVICE = ''
    PREV_DIR = ''

    def __init__(self):
        super().__init__()
        # APP TITLE
        self.title("Report app")

        # FIXED APP SIZE
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(0, 0)

        # BIND CLOSING COMMAND => (Ctrl + q)
        self.bind("<Command-q>", self.on_closing)

        # REMOVE TITLE BAR
        self.overrideredirect(True)

        # BACKGROUND COLOR
        self.configure(bg="#262626")

        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call when app gets closed

        self.setPrevDIR()

        # TODO : MAKE WINDOW DRAGGABLE

        # CREATE CONTAINER
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # & ROW 1
        # * LOGO + CLOSING BUTTON
        # ^ CLOSING BUTTON
        self.Close_Button = customtkinter.CTkButton(
            master=self,
            command=self.on_closing,
            text="X",
            text_font="none 12",
            text_color="#c75d55",
            hover=True,
            hover_color="black",
            height=35,
            width=60,
            border_width=2,
            corner_radius=3,
            border_color="#c75d55",
            bg_color="#262626",
            fg_color="#262626")

        # ^ PLACING
        self.Close_Button.place(x=715, y=20)

        # & ROW 1
        # * FILE INPUT + FILENAME LABEL + FILE TITLE LABEL
        self.FilenameLabel = customtkinter.CTkLabel(
            height=42,
            text="Connected Devices",
            text_font="none 12",
            text_color="#3b8cc6",
        )

        self.FilenameLabel.place(x=36, y=60)

        # & ROW 2
        # * FILE INPUT + FILENAME LABEL + FILE TITLE LABEL
        self.BrowseFile = customtkinter.CTkButton(
            master=self,
            command=self.browseFiles,
            text="Browse File",
            text_font="none 12",
            text_color="#3b8cc6",
            hover=True,
            hover_color="black",
            height=40,
            width=120,
            border_width=2,
            corner_radius=3,
            border_color="#68aec9",
            bg_color="#262626",
            fg_color="#262626"
        )

        self.FilenameLabel = customtkinter.CTkLabel(
            height=42,
            text="No File chosen",
            text_font="none 12",
            text_color="#3b8cc6",
        )

        self.BrowseFile.place(x=36, y=120)
        self.FilenameLabel.place(x=158, y=120)

        # & ROW 3
        # * SEND BUTTON + FEEDBACK LABEL
        self.Send_Button = customtkinter.CTkButton(
            master=self,
            command=self.push_button_event,
            text="SEND FILE",
            text_font="none 12",
            text_color="#3b8cc6",
            hover=True,
            hover_color="black",
            height=40,
            width=120,
            border_width=2,
            corner_radius=3,
            border_color="#68aec9",
            bg_color="#262626",
            fg_color="#262626")

        self.SuccessFeedbackLabel = customtkinter.CTkLabel(
            height=42,
            text="File Was Sent Successfully",
            text_font="none 12",
            text_color="#79ae61",
        )

        self.FailFeedbackLabel = customtkinter.CTkLabel(
            height=42,
            text_font="none 12",
            text_color="#c75d55",
        )

        # ^ PLACING
        self.Send_Button.place(x=36, y=190)

        # & THIRD ROW
        # * GET BUTTON + FEEDBACK LABEL
        self.Get_Button = customtkinter.CTkButton(
            master=self,
            command=self.pull_button_event,
            text="GET FILE",
            text_font="none 12",
            text_color="#3b8cc6",
            hover=True,
            hover_color="black",
            height=40,
            width=120,
            border_width=2,
            corner_radius=3,
            border_color="#68aec9",
            bg_color="#262626",
            fg_color="#262626")

        # ^ PLACING
        self.Get_Button.place(x=36, y=350)

    # ^ FUNCTIONS

    def on_closing(self, event=0):
        self.destroy()

    # ^ ============== ADB FUNCTIONS ========================

    def pull_button_event(self):
        file_path = os.path.expanduser('~')
        pull_command = f"adb pull /storage/emulated/0/Download/NewCounter.txt {file_path}\Desktop"
        with subprocess.Popen(pull_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            print(output)

    def push_button_event(self):
        print(f"bool is {App.FILE_TO_SEND != ''}")
        if (App.FILE_TO_SEND != ''):
            connect_command = "adb get-state"
            subprocess.call(connect_command, shell=True)

            # if (App.DEVICE != ''):
            pull_command = (
                f"adb push {App.FILE_TO_SEND} /storage/emulated/0/Download/"
            )
            subprocess.call(pull_command, shell=True)
            self.SuccessFeedbackLabel.place(x=172, y=190)
            # CHECK IF FILE EXISTS IN THE DEVICE
            # No Device
            # else:
            #     self.FailFeedbackLabel.configure(
            #         text="No Devices are connected, connect to device and try again.",)
            #     self.FailFeedbackLabel.place(x=172, y=190)
        else:
            # No file chosen
            self.FailFeedbackLabel.configure(
                text="No File chosen, choose file and try again.",)
            self.FailFeedbackLabel.place(x=172, y=190)

    # ^ ============== FILE FUNCTIONS ========================
    def browseFiles(self):
        initialDIR = App.PREV_DIR if App.PREV_DIR != '' else '/'
        App.FILE_TO_SEND = filedialog.askopenfilename(initialdir=initialDIR,
                                                      title="Select a File",
                                                      filetypes=(("Excel Files",
                                                                  "*.xlsx*"),
                                                                 ("all files",
                                                                  "*.*")))
        # ^ GET PREVIOUS DIRECTORY
        # TODO : SAVE DIRECTORY TO A FILE FOR RELOAD
        if (App.FILE_TO_SEND != ''):
            temp = App.FILE_TO_SEND.split('/')
            App.PREV_DIR = "/".join(temp[:-1])
            # ^ SAVING FOR WHEN APP IS RELOADED
            if not os.path.exists(".report_preferences/"):
                os.mkdir(".report_preferences/")

            with open('.report_preferences/.preferences.txt', 'w') as f:
                f.write(f'PREV_DIR={App.PREV_DIR}')

            self.setPrevDIR()

        print(f"File_TO_SEND IS {App.FILE_TO_SEND}")
        # Change label contents
        self.FilenameLabel.configure(text="File Opened: "+App.FILE_TO_SEND)

    def setPrevDIR(self):
        preference_file = '.report_preferences/.preferences.txt'
        if (os.path.exists(preference_file) and os.path.isfile(preference_file)):
            with open(preference_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'PREV_DIR' in line:
                        previous_dir = line.split('=')[1]
                        if (previous_dir):
                            App.PREV_DIR = previous_dir
                        else:
                            App.PREV_DIR = "/"


if __name__ == "__main__":
    app = App()
    app.mainloop()
