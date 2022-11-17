import tkinter as tk
import tkinter
import customtkinter
from tkinter import filedialog
import subprocess
from pathlib import Path
import os

# LOCAL MODULES
# from logic import *


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
    CHOSEN_FILE = ''

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

        # open previous dir on startup if there was any
        self.setPrevDIR()

        # DEFINE OUR 3 ROWS

        # & DEFINITIONS

        # * TOP FRAME
        self.frame_top = customtkinter.CTkFrame(
            master=self, width=750,
            height=100)
        self.frame_top.grid(row=0, column=0, padx=25, pady=15, sticky="nswe")
        self.frame_top.grid_propagate(0)  # make frame constant size

        # * MIDDLE FRAME
        self.frame_middle = customtkinter.CTkFrame(
            master=self, width=750,
            height=190)
        self.frame_middle.grid(row=1, column=0, padx=25,
                               pady=10, sticky="nswe")
        self.frame_middle.grid_propagate(0)  # make frame constant size

        # * BOTTOM FRAME
        self.frame_bottom = customtkinter.CTkFrame(
            master=self, width=750, height=180)
        self.frame_bottom.grid(
            row=2, column=0, padx=25, pady=10, sticky="nswe")
        self.frame_bottom.grid_propagate(0)  # make frame constant size

        # & CONFIGURE GRIDS AND ELEMENTS

        # ^ TOP ROW FRAME
        check_conn = Buttons(self.frame_top, self.check_devices,
                             "Check Device", "#3b8cc6", "#68aec9")
        self.DeviceBTN = check_conn.newButton()

        device_label = Lables(
            self.frame_top, "No Device is Connected", label_type="error")
        self.DeviceLabel = device_label.newLabel()

        self.frame_top.grid_rowconfigure(0, minsize=20)
        self.frame_top.grid_columnconfigure(0, minsize=20)

        self.DeviceBTN.grid(row=1, column=1)
        self.frame_top.grid_columnconfigure((1, 2), minsize=20)

        #  ^ MIDDLE ROW FRAME
        browse_btn = Buttons(self.frame_middle, self.browseFiles,
                             "Browse File", "#3b8cc6", "#68aec9")
        self.BrowseFile = browse_btn.newButton()

        filename_label = Lables(
            self.frame_middle, "No File chosen", label_type="info")
        self.FilenameLabel = filename_label.newLabel()

        send_btn = Buttons(self.frame_middle, self.push_button_event,
                           "Send File", "#3b8cc6", "#68aec9")
        self.SendFile = send_btn.newButton()
        self.SendFile.configure(state="disabled", text_color="#3b8cc6")

        success_label = Lables(
            self.frame_middle, "File Was Sent Successfully", label_type="success")
        self.SuccessFeedbackLabel = success_label.newLabel()

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_middle, height=14,
                                                     text="Keep chosen file", border_color="#79ae61",
                                                     text_color="#79ae61", checkmark_color="green", command=self.keepFile)

        self.frame_middle.grid_rowconfigure(0, minsize=10)
        self.frame_middle.grid_columnconfigure(0, minsize=0)

        self.BrowseFile.grid(row=1, column=1)
        self.frame_top.grid_columnconfigure((1, 2), minsize=20)
        self.FilenameLabel.grid(row=1, column=3, sticky="nwsw")

        self.check_box_2.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        # self.FailFeedbackLabel.grid(row=2, column=1, sticky="nwsw")

        self.frame_middle.grid_rowconfigure(3, minsize=5)

        self.SendFile.grid(row=4, column=1)
        self.frame_top.grid_columnconfigure((4, 2), minsize=20)
        self.SuccessFeedbackLabel.grid(row=4, column=3, sticky="nwsw")

        #  ^ BOTTOM ROW FRAME
        get_btn = Buttons(self.frame_bottom, self.push_button_event,
                          "Get File", "#3b8cc6", "#68aec9")
        self.GetFile = get_btn.newButton()

        file_label = Lables(
            self.frame_bottom, "Error or success feedbacks", label_type="error")
        self.getFileLabel = file_label.newLabel()

        self.frame_bottom.grid_rowconfigure(0, minsize=20)
        self.frame_bottom.grid_columnconfigure(0, minsize=20)

        self.GetFile.grid(row=1, column=1)
        self.frame_bottom.grid_columnconfigure((1, 2), minsize=20)
        self.getFileLabel.grid(row=1, column=3, sticky="w")

    # ^ ============== ADB METHODS ========================
    def check_devices(self):
        devices_command = f"adb devices"
        with subprocess.Popen(devices_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            if ("List" in output):
                device_name = output.split(" ")[3]
                self.DeviceLabel.configure(
                    text="Device Attached " + device_name)
                self.DeviceLabel.grid(row=1, column=3, sticky="w")
                device_str = (
                    ' '.join(str(output.split(" ")[3]).split())).split(" ")[1]

                BasicConfig.DEVICE = device_str
                self.DeviceLabel.configure(
                    text="Device attached : "+device_str, text_color="#79ae61")
                self.DeviceLabel.grid(row=1, column=3, sticky="w")
            else:
                pass
                self.DeviceLabel.configure(text="There is no device attached")
                self.DeviceLabel.grid(row=1, column=3, sticky="w")
                BasicConfig.DEVICE = ""
                print("Success")

    def pull_button_event(self):
        file_path = os.path.expanduser('~')
        pull_command = f"adb pull /storage/emulated/0/Download/NewCounter.txt {file_path}\Desktop"
        with subprocess.Popen(pull_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            print(output)

    def push_button_event(self):
        print(f"bool is {BasicConfig.FILE_TO_SEND != ''}")
        if (BasicConfig.FILE_TO_SEND != ''):
            connect_command = "adb get-state"
            subprocess.call(connect_command, shell=True)

            if (BasicConfig.DEVICE != ''):
                pull_command = (
                    f"adb push {BasicConfig.FILE_TO_SEND} /storage/emulated/0/Download/"
                )
                subprocess.call(pull_command, shell=True)
                self.SuccessFeedbackLabel.place(x=172, y=190)
            # CHECK IF FILE EXISTS IN THE DEVICE
            # No Device
            else:
                self.FailFeedbackLabel.configure(
                    text="No Devices are connected, connect to device and try again.",)
                self.FailFeedbackLabel.place(x=172, y=190)
        else:
            # No file chosen
            self.FailFeedbackLabel.configure(
                text="No File chosen, choose file and try again.",)
            self.FailFeedbackLabel.place(x=172, y=190)
    # ^ ============== FILE METHODS ========================

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
        self.SendFile.configure(
            state="active", hover_color="black")

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

    def keepFile(self):
        BasicConfig.CHOSEN_FILE = BasicConfig.FILE_TO_SEND if BasicConfig.CHOSEN_FILE == '' else ''
        print(BasicConfig.CHOSEN_FILE)


class Buttons(customtkinter.CTk):
    def __init__(self, master, command, text, color, border_color) -> None:
        self.master = master
        self.command = command
        self.text = text
        self.color = color
        self.border_color = border_color

    def newButton(self):
        return customtkinter.CTkButton(
            master=self.master,
            command=self.command,
            text=self.text,
            text_font="none 12",
            text_color=self.color,
            hover=True,
            hover_color="black",
            height=40,
            width=120,
            border_width=2,
            corner_radius=3,
            border_color=self.border_color,
            bg_color="#262626",
            fg_color="#262626"
        )


class Lables(customtkinter.CTk):
    def __init__(self, master, text, label_type="") -> None:
        self.master = master
        self.text = text
        self.label_type = label_type

    def newLabel(self):
        if (self.label_type == "success"):
            self.text_color = "#79ae61"
        elif (self.label_type == "error"):
            self.text_color = "#c75d55"
        elif (self.label_type == "info"):
            self.text_color = "#68aec9"
        return customtkinter.CTkLabel(
            master=self.master,
            text=self.text,
            height=42,
            text_font="none 12",
            text_color=self.text_color,
        )
