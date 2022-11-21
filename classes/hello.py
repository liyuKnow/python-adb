from tkinter import *
import tkinter as tk
import customtkinter

from widgets import HelloButton, Window


def main():
    root = Tk()
    # 'width x height + X-position + y-position'
    window1 = Window(root, "Class Based Window",
                     '400x400+90+120', "hello class based window")

    root.mainloop()
    return None


if __name__ == "__main__":
    main()
