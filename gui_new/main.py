import tkinter as tk  # GUI toolkit
from tkinter import ttk
import os 
import random 


def getRandomCol():
    
    r = hex(random.randrange(0, 255))[2:]
    g = hex(random.randrange(0, 255))[2:]
    b = hex(random.randrange(0, 255))[2:]

    random_col = '#'+r+g+b
    return random_col



os.environ.__setitem__('DISPLAY', ':0.0')
root = tk.Tk()
root.geometry("900x600")

cols = 4
rows = 2

frames = {}

for r in range(0, rows):
    for c in range(0, cols):
        frames.update( { (r, c) : tk.Frame(root, background="#FFF0C1", bd=1, relief="sunken" ) } )
        frames.get((r, c)).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)


for r in range(0, rows):
    root.grid_rowconfigure(r, weight=3)


for c in range(0, cols):
    root.grid_columnconfigure(c, weight=2)


camera_frame = tk.Frame(root) 

button1 = tk.Button(camera_frame, text ="button", fg ="orange")
button1.pack(side = tk.TOP) 
entry_name = tk.Entry(camera_frame, textvariable=tk.StringVar())
entry_name.pack(side=tk.TOP)


frames.update({ (0,0) : camera_frame } )
frames.get((0, 0)).grid(row=0, column=0, sticky="nsew", padx=2, pady=2)



root.mainloop()

