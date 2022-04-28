
import tkinter as tk  # GUI toolkit
from PIL import Image, ImageTk  # GUI images
import os.path  # path operations
from platform import system  # returns the system/OS name
import time  # time access and conversions
import tkinter.messagebox
from tkinter import simpledialog

from tkinter import ttk

os.environ.__setitem__('DISPLAY', ':0.0')

class Manager_ui():
    def __init__(self, root_, master_obj):
        self.master_obj = master_obj
        self.root = root_
        
        self.root.geometry("230x300")

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)

        self.frame_edit = tk.Frame(self.root, background="grey", bd=1, relief="sunken" )
        self.frame_edit.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.frame_edit.columnconfigure(0, weight = 1)
        self.frame_edit.columnconfigure(1, weight = 1)
        self.frame_edit.columnconfigure(2, weight = 1)
        self.frame_edit.rowconfigure(0, weight = 1)

        self.edit_add = tk.Button(self.frame_edit, text = "+", command=self.add_callback)
        self.edit_add.grid(row=0, column=2, sticky='nesw')
        self.edit_edit = tk.Button(self.frame_edit, text = "edit", command=self.edit_callback)
        self.edit_edit.grid(row=0, column=1, sticky='nesw')
        self.edit_remove = tk.Button(self.frame_edit, text = "-", command=self.remove_callback)
        self.edit_remove.grid(row=0, column=0, sticky='nesw')

        self.frame_list = tk.Frame(self.root, background="grey", bd=1, relief="sunken" )
        self.frame_list.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.frame_list.rowconfigure(0, weight = 1)
        self.frame_list.columnconfigure(0, weight = 1)

        self.selected_modules_listbox = tk.Listbox(self.frame_list)
        self.selected_modules_listbox.grid(row=0, column=0, sticky='nesw')
        self.selected_modules_listbox.insert(1, "1")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=25)
        self.root.grid_columnconfigure(0, weight=1)

        self.path = str(os.getcwd())

        self.selected_modules = []
        
        self.options = []
        #self.root.mainloop()

    # button callbacks
    # ------------------------------------------------------------------------------------------------------------------

    def edit_callback(self):
        pass

    def add_callback(self):
        wanted_module, wanted_name, wanted_ip, wanted_location = self.popup(self.options) 
        print("inputted location: ", wanted_location)
        self.master_obj.add_module(wanted_module, wanted_name, wanted_ip, wanted_location)
        #self.selected_modules_listbox.insert(1, wanted_name)
        #wanted_class = self.options1.get(wanted_module)
        #instance = wanted_class(self.frame_content)
        #self.add_module(instance)
        pass

 
    def remove_callback(self):
        #for i in self.selected_modules_listbox.curselection():
        #    print(self.selected_modules_listbox.get(i))
        
        self.master_obj.remove_module(self.selected_modules_listbox.get(self.selected_modules_listbox.curselection()))
        self.selected_modules_listbox.delete(self.selected_modules_listbox.curselection())

        #print(self.selected_modules_listbox.curselection())
        

    def popup(self, options):
        dialog = MyDialog(title=".", parent=self.root, options=options)
        return dialog.my_module, dialog.my_name, dialog.my_ip, dialog.my_location


    def add_module(self, ui_frame):
        ui_frame.pack(side = "left")


    def edit_module(self):
        wanted_module, wanted_name, wanted_ip = self.popup(self.options) 
        print(wanted_module)
        wanted_class = self.options1.get(wanted_module)
        instance = wanted_class(self.frame_content)
        self.add_module(instance)
        

    def remove_ui(self, module):
        module.get_ui().pack_forget()

    def set_optional_modules(self, modules):
        self.options = modules
    
    


   









class MyDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title, options):
        self.options = options
        self.my_name = None
        self.my_ip = None
        self.my_module = None
        self.my_location = None
        super().__init__(parent, title)

    def body(self, frame):
        clicked = tk.StringVar(frame)


        self.module = ttk.Combobox(frame, textvariable=clicked)
        self.module['values'] = self.options
        self.module.pack()
        # print(type(frame)) # tkinter.Frame
        self.my_name_label = tk.Label(frame, width=25, text="name")
        self.my_name_label.pack()
        self.my_name_entry = tk.Entry(frame, width=25)
        self.my_name_entry.pack()

        self.my_ip_label = tk.Label(frame, width=25, text="ip")
        self.my_ip_label.pack()
        self.my_ip_entry = tk.Entry(frame, width=25)
        self.my_ip_entry.pack()

        self.my_location_label = tk.Label(frame, width=25, text="location")
        self.my_location_label.pack()
        self.my_location_entry = tk.Entry(frame, width=25)
        self.my_location_entry.pack()
        

        return frame

    def ok_pressed(self):
        # print("ok")
        self.my_name = self.my_name_entry.get()
        self.my_ip = self.my_ip_entry.get()
        self.my_module = self.module.get()
        self.my_location = int(self.my_location_entry.get())
        self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.destroy()


    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())