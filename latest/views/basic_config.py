import tkinter as tk
import tkinter
import customtkinter
from tkinter import filedialog
import os


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


class BasicConfig(customtkinter.CTk):
    WIDTH = 800
    HEIGHT = 550
    FILE_TO_SEND = ''
    FILE_TO_GET = ''
    DEVICE = ''
    PREV_DIR = ''

    def __init__(self):
        super().__init__()
        # APP TITLE
        self.title("Report app")

        # FIXED APP SIZE
        self.minsize(BasicConfig.WIDTH, BasicConfig.HEIGHT)
        self.maxsize(BasicConfig.WIDTH, BasicConfig.HEIGHT)

        # CHANGE APP ICON
        # self.iconphoto(False, tk.PhotoImage(file="assets/title_icon.png"))

        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # TODO BASIC CONFIG ENDS HERE THE FRAMES AND THEIR COMPONENTS SHOULD BE SEPARATED
        # DEFINE OUR 3 ROWS

        # * DEFINITIONS
        self.frame_top = customtkinter.CTkFrame(
            master=self, width=750,
            height=100)
        self.frame_top.grid(row=0, column=0, padx=25, pady=15, sticky="nswe")
        self.frame_top.grid_propagate(0)  # make frame constant size

        self.frame_middle = customtkinter.CTkFrame(
            master=self, width=750,
            height=190)
        self.frame_middle.grid(row=1, column=0, padx=25,
                               pady=10, sticky="nswe")
        self.frame_middle.grid_propagate(0)  # make frame constant size

        self.frame_bottom = customtkinter.CTkFrame(
            master=self, width=750, height=180)
        self.frame_bottom.grid(
            row=2, column=0, padx=25, pady=10, sticky="nswe")
        self.frame_bottom.grid_propagate(0)  # make frame constant size
        # * CONFIGURE GRIDS
        # ^ TOP ROW FRAME
        # #  ^ MIDDLE ROW FRAME

        # #  ^ BOTTOM ROW FRAME

        # * SET COMPONENTS/WIDGETS
        #  ^ TOP ROW FRAME
        #  ^ MIDDLE ROW FRAME
        self.BrowseFile = customtkinter.CTkButton(
            master=self.frame_middle,
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
            master=self.frame_middle,
            height=42,
            text="No File chosen",
            text_font="none 12",
            text_color="#3b8cc6",
        )

        self.Send_Button = customtkinter.CTkButton(
            master=self.frame_middle,
            command=self.browseFiles,
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
            master=self.frame_middle,
            height=42,
            text="File Was Sent Successfully",
            text_font="none 12",
            text_color="#79ae61",
        )

        self.FailFeedbackLabel = customtkinter.CTkLabel(
            self.frame_middle,
            height=42,
            text_font="none 12",
            text_color="#c75d55",
        )

        # ROW 1 COLUMN 1 and 2
        self.frame_middle.grid_rowconfigure(0, minsize=20)
        self.frame_middle.grid_columnconfigure(0, minsize=20)

        self.BrowseFile.grid(row=1, column=1)
        self.FilenameLabel.grid(row=1, column=2, sticky="w")

        self.FailFeedbackLabel.grid(row=2, column=1,)

        self.frame_middle.grid_rowconfigure(3, minsize=5)

        self.Send_Button.grid(row=4, column=1)
        self.SuccessFeedbackLabel.grid(row=4, column=2,)

        #  ^ BOTTOM ROW FRAME

    # ^ ============== FILE FUNCTIONS ========================
    def browseFiles(self):
        initialDIR = BasicConfig.PREV_DIR if BasicConfig.PREV_DIR != '' else '/'
        BasicConfig.FILE_TO_SEND = filedialog.askopenfilename(initialdir=initialDIR,
                                                              title="Select a File",
                                                              filetypes=(("Excel Files",
                                                                          "*.xlsx*"),
                                                                         ("all files",
                                                                          "*.*")))
        # ^ GET PREVIOUS DIRECTORY
        # TODO : SAVE DIRECTORY TO A FILE FOR RELOAD
        if (BasicConfig.FILE_TO_SEND != ''):
            temp = BasicConfig.FILE_TO_SEND.split('/')
            BasicConfig.PREV_DIR = "/".join(temp[:-1])
            # ^ SAVING FOR WHEN APP IS RELOADED
            if not os.path.exists(".report_preferences/"):
                os.mkdir(".report_preferences/")

            with open('.report_preferences/.preferences.txt', 'w') as f:
                f.write(f'PREV_DIR={BasicConfig.PREV_DIR}')

            self.setPrevDIR()

        print(f"File_TO_SEND IS {BasicConfig.FILE_TO_SEND}")
        # Change label contents
        self.FilenameLabel.configure(
            text="File Opened: "+BasicConfig.FILE_TO_SEND)

    def setPrevDIR(self):
        preference_file = '.report_preferences/.preferences.txt'
        if (os.path.exists(preference_file) and os.path.isfile(preference_file)):
            with open(preference_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'PREV_DIR' in line:
                        previous_dir = line.split('=')[1]
                        if (previous_dir):
                            BasicConfig.PREV_DIR = previous_dir
                        else:
                            BasicConfig.PREV_DIR = "/"


class TopFrame():
    pass


class MiddleFrame():
    pass


class BottomFrame():
    pass
