import tkinter
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

import win32gui
import win32api
from win32con import SWP_NOMOVE 
from win32con import SWP_NOSIZE 
from win32con import SW_HIDE
from win32con import SW_SHOW
from win32con import HWND_TOPMOST
from win32con import GWL_EXSTYLE 
from win32con import WS_EX_TOOLWINDOW


class Win(tkinter.Tk):

    def __init__(self,master=None):
        tkinter.Tk.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)
        self.bind('<space>w',self.closewin)

        self.attributes("-topmost", True)
        background_label = Label(self, text="ヤサミンのお尻をファック", font=("Arial", 8), fg="pink", bg="#cc99a2")
        background_image=PhotoImage(file="rounded-yas.png")
        background_label_image = Label(self, image=background_image, bg='#cc99a2')
        self.lift()
        self.wm_attributes("-transparentcolor", "#cc99a2")
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.place(relx=0.12, rely=1.0, anchor='sw')
        background_label_image.place(relx=0.0, rely=1.0, anchor='sw')
        background_label_image.image = background_image

        w = 170
        h = 20
        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        # y = (hs/2) - (h/2)
        # x = 99
        y = 40
        # self._offsetx = x
        # self._offsety = y

        # set the dimensions of the screen 
        # and where it is placed
        handler = self.find_window("tk")
        self.hide_from_taskbar(handler)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.set_topmost(handler)

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y
    
    def closewin(self, event):
        self.destroy()
    
    @staticmethod
    def find_window(name):
        try:
            return win32gui.FindWindow(None, name)
        except win32gui.error:
            print("Error while finding the window")
            return None

    @staticmethod   
    def hide_from_taskbar(hw):
        try:
            win32gui.ShowWindow(hw, SW_HIDE)
            win32gui.SetWindowLong(hw, GWL_EXSTYLE,win32gui.GetWindowLong(hw, GWL_EXSTYLE)| WS_EX_TOOLWINDOW);
            win32gui.ShowWindow(hw, SW_SHOW);
        except win32gui.error:
            print("Error while hiding the window")
            return None

    @staticmethod
    def set_topmost(hw):
        try:
            win32gui.SetWindowPos(hw, HWND_TOPMOST, 0,0,0,0, SWP_NOMOVE | SWP_NOSIZE)
        except win32gui.error:
            print("Error while move window on top")


win = Win()
win.mainloop()