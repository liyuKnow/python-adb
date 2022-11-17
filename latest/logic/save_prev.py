import os
from tkinter import filedialog


def browseFiles(dir_constant, file_constant, file_name_label):
    initialDIR = dir_constant if dir_constant != '' else '/'
    file_constant = filedialog.askopenfilename(initialdir=initialDIR,
                                               title="Select a File",
                                               filetypes=(("Excel Files",
                                                           "*.xlsx*"),
                                                          ("all files",
                                                           "*.*")))
    # ^ GET PREVIOUS DIRECTORY
    # TODO : SAVE DIRECTORY TO A FILE FOR RELOAD
    if (file_constant != ''):
        temp = file_constant.split('/')
        dir_constant = "/".join(temp[:-1])
        # ^ SAVING FOR WHEN APP IS RELOADED
        if not os.path.exists(".report_preferences/"):
            os.mkdir(".report_preferences/")

        with open('.report_preferences/.preferences.txt', 'w') as f:
            f.write(f'PREV_DIR={dir_constant}')

        setPrevDIR()

    print(f"File_TO_SEND IS {file_constant}")
    # Change label contents
    file_name_label.configure(text="File Opened: "+file_constant)


def setPrevDIR():
    preference_file = '.report_preferences/.preferences.txt'
    if (os.path.exists(preference_file) and os.path.isfile(preference_file)):
        with open(preference_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'PREV_DIR' in line:
                    previous_dir = line.split('=')[1]
                    if (previous_dir):
                        dir_constant = previous_dir
                    else:
                        dir_constant = "/"
