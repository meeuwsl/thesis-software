import tkinter as tk  # GUI toolkit
from tkinter import ttk
import os 
import random 

os.environ.__setitem__('DISPLAY', ':0.0')


class Control_ui():
    def __init__(self, root_, master_obj):
        self.root = tk.Toplevel(root_)
        self.root.geometry("700x600")
        self.cols = 4
        self.rows = 2

        self.frames = {}

        for r in range(0, self.rows):
            for c in range(0, self.cols):
                self.frames.update( { (r, c) : tk.Frame(self.root, background="#FFF0C1", bd=1, relief="sunken" ) } )
                self.frames.get((r, c)).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)


        for r in range(0, self.rows):
            self.root.grid_rowconfigure(r, weight=3)


        for c in range(0, self.cols):
            self.root.grid_columnconfigure(c, weight=2)


        # self.camera_frame = tk.Frame(self.root) 



        # self.frames.update({ (0,0) : self.camera_frame } )
        # self.frames.get((0, 0)).grid(row=0, column=0, sticky="nsew", padx=2, pady=2)



        #self.root.mainloop()


    def add_module_ui(self, frame, position):
        

        self.frames.update({ position : frame } )
        self.frames.get(position).grid(row=0, column=0, sticky="nsew", padx=2, pady=2)


