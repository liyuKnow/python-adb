# import os
# import ctypes


# def check_prep(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         FILE_ATTRIBUTE_HIDDEN = 0x02
#         ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)


# path = "hello/ji"
# check_prep(path)

import os
os.mkdir(".report_preferences/")

with open('.report_preferences/.preferences.txt', 'w') as f:
    f.write('PREV-DIR=')
