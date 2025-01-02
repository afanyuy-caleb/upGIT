import os, sys
from tkinter import *
from tkinter import filedialog, font
import tkinter.messagebox as messageBox
from PIL import Image, ImageTk

class HomePage():
    def __init__(self, root, user_info):
        self.window = root
        self.user_info = user_info
        self.render()
    
    def render(self):
        self.window.title("upGIT Dashboard")
        username = self.user_info.name
        homeLabel = Label(self.window, text=f"Welcome {username}", font=('Poppins', 18, 'bold'), bg="white")
        homeLabel.place(relx=0.25, rely=0.15)