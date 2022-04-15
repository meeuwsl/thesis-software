import tkinter as tk  # GUI toolkit
from tkinter import ttk
import os 
import random 

os.environ.__setitem__('DISPLAY', ':0.0')


class Control_ui():
    def __init__(self, master_obj):
        self.root = tk.Tk()
        self.root.geometry("900x600")
        
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


        self.camera_frame = tk.Frame(self.root) 

        self.button1 = tk.Button(self.camera_frame, text ="button", fg ="orange")
        self.button1.pack(side = tk.TOP) 
        self.entry_name = tk.Entry(self.camera_frame, textvariable=tk.StringVar())
        self.entry_name.pack(side=tk.TOP)


        self.frames.update({ (0,0) : self.camera_frame } )
        self.frames.get((0, 0)).grid(row=0, column=0, sticky="nsew", padx=2, pady=2)



        self.root.mainloop()

