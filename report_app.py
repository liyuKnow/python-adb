from tkinter import *
import customtkinter
import subprocess
# import filedialog module
from tkinter import filedialog


class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 600

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

        # & ROW 2
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
            command=self.push_button_event,
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
            text="Something went wrong while sending file",
            text_font="none 12",
            text_color="#c75d55",
        )

        # ^ PLACING
        self.Send_Button.place(x=36, y=190)
        self.SuccessFeedbackLabel.place(x=172, y=190)

        # & THIRD ROW
        # * GET BUTTON + FEEDBACK LABEL
        self.Get_Button = customtkinter.CTkButton(
            master=self,
            command=self.push_button_event,
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
        pull_command = "adb pull /storage/emulated/0/Download/usersDownload.xlsx C:/Users/Liyu/Desktop"
        subprocess.call(pull_command, shell=True)
        print("Success")

    def push_button_event(self):
        pull_command = (
            "adb push C:/Users/Liyu/Desktop/VeryNew.xlsx /storage/emulated/0/Download/"
        )
        subprocess.call(pull_command, shell=True)
        print("Success")


if __name__ == "__main__":
    app = App()
    app.mainloop()
