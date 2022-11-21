from tkinter import *
import tkinter as tk
import customtkinter


class HelloButton():
    def __init__(self, master):

        frame = Frame(master=master)
        frame.pack()

        self.printButton = Button(
            frame, text="Press me Boo!", command=self.printMessage)
        self.printButton.pack(side=LEFT)

    def printMessage(self):
        print("Wooo Hooo! It works")
