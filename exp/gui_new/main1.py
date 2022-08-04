import tkinter as tk  # GUI toolkit
from tkinter import ttk
import os 
import random 

os.environ.__setitem__('DISPLAY', ':0.0')
root = tk.Tk()


root.geometry("230x300")

def donothing():
    pass


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

frame_edit = tk.Frame(root, background="grey", bd=1, relief="sunken" )
frame_edit.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
frame_edit.columnconfigure(0, weight = 1)
frame_edit.columnconfigure(1, weight = 1)
frame_edit.columnconfigure(2, weight = 1)
frame_edit.rowconfigure(0, weight = 1)

edit_add = tk.Button(frame_edit, text = "+", command=donothing)
edit_add.grid(row=0, column=2, sticky='nesw')
edit_edit = tk.Button(frame_edit, text = "edit", command=donothing)
edit_edit.grid(row=0, column=1, sticky='nesw')
edit_remove = tk.Button(frame_edit, text = "-", command=donothing)
edit_remove.grid(row=0, column=0, sticky='nesw')

frame_list = tk.Frame(root, background="grey", bd=1, relief="sunken" )
frame_list.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=25)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

