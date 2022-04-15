
import tkinter as tk  # GUI toolkit
from PIL import Image, ImageTk  # GUI images
import os.path  # path operations
from platform import system  # returns the system/OS name
import time  # time access and conversions
import tkinter.messagebox
from tkinter import simpledialog




from tkinter import ttk

os.environ.__setitem__('DISPLAY', ':0.0')

class Manager_ui(tk.Tk):
    def __init__(self, master, master_obj):
        self.master_obj = master_obj
        self.root = master
        super().__init__()  # call tk.Tk.__init__() to initialize tkinter object
        
        # window configuration
        self.configure(background="white")
        self.attributes("-fullscreen", False) # full screen window
        self.path = str(os.getcwd())
        # fonts
        self.my_font_title = ('Akkurat TT Light', 25)
        self.my_font = ('Helvetica', 11)
        self.my_font_bold = ('Helvetica', 11, "bold")
        self.my_font_italic = ('Helvetica', 11, "italic")

        # colors (HEX)
        self.color_absolem_green = "#6BC2B4"
        self.color_absolem_lightblue = "#54779A"
        self.color_absolem_darkblue = "#1B4093"
        self.color_absolem_grey = "#EDEDED"
        self.color_absolem_green_automation = "#9DD1B7"
        self.color_absolem_blue_innovation = "#8ECCE2"
        self.color_absolem_blue_industry = "#ADD3DE"
        self.color_absolem_blue_prototype = "#6C97C1"
        # --------------------------------------------------------------------------------------------------------------
        # frames
        self.frame_content = tk.Frame(self, background="white")
        self.frame_buttons = tk.Frame(self, width=500, height=100, background="grey")
        self.frame_buttons.columnconfigure(0, weight=1)
        self.frame_buttons.rowconfigure(0, weight=1)
        self.frame_buttons.grid_propagate(0)

        
        
        # --------------------------------------------------------------------------------------------------------------
        # quit
        self.labelframe_quit = tk.LabelFrame(self.frame_buttons, text="quit", font=self.my_font,
                                                background="white")
        self.button_labelframe_quit = tk.Button(self.labelframe_quit, text="quit", height=2, width=2,
                                             font=self.my_font, background=self.color_absolem_green_automation,
                                             command=self.button_quit_callback)
        
        self.button_labelframe_quit.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.labelframe_quit.grid(row=0, column=0, padx=5, pady=5, sticky="nw")



        self.module1 = tk.LabelFrame(self.frame_content, text="module 1", font=self.my_font, background="white")
        self.b = tk.Button(self.module1, text = "module1", height = 2, width = 2)
      
        # drop down with optional modules 
        self.b_add_module = tk.Button(self.frame_content, text = "add", command=self.add_callback)
        self.b_remove_module = tk.Button(self.frame_content, text = "remove", command=self.remove_callback)
        self.b_edit_module = tk.Button(self.frame_content, text = "edit", command=self.edit_callback)
        self.b_test = tk.Button(self.frame_content, text = "test", command=self.master_obj.test1)

        # list of selected modules
        self.selected_modules = []
        self.selected_modules_listbox = tk.Listbox(self.frame_content)

        # call initialization class methods
        self.geometry_manager()

    def geometry_manager(self):
        """
        Control the application layout using tk.pack(), tk.place() and tk.grid()
        """
        # --------------------------------------------------------------------------------------------------------------
        # frames
        #self.frame_content.pack(side="bottom", fill="both", expand=True, padx=5, pady=(0, 5))
        self.frame_content.pack(side = "bottom")
        self.frame_buttons.pack(side = "top")
        # --------------------------------------------------------------------------------------------------------------

        # labelframe with buttons
        # --------------------------------------------------------------------------------------------------------------


        # modules 
        #self.module1.grid(row = 0, column = 1, padx=5, pady=5, sticky="nw")
        #self.b.grid(row = 0, column = 1, padx=5, pady=5, sticky="nw")

        self.b_add_module.pack(side = "bottom")
        self.b_remove_module.pack(side = "bottom")
        self.b_edit_module.pack(side = "bottom")
        self.b_test.pack(side = "bottom")

        self.selected_modules_listbox.pack(side = "bottom")


    # button callbacks
    # ------------------------------------------------------------------------------------------------------------------
    def button_quit_callback(self):
        self.destroy()

    def stop(self):
        self.destroy()



    def edit_callback(self):
        pass

    def add_callback(self):
        wanted_module, wanted_name, wanted_ip = self.popup(self.options) 
        print(wanted_module)
        self.master_obj.add_module(wanted_module, wanted_name, wanted_ip)
        #popup = Popup()
#        print(popup.get_value(options))
        self.selected_modules_listbox.insert(1, wanted_name)
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
        #clicked = tk.StringVar()

        #self.drop_down = ttk.Combobox(self.frame_content, values = self.options)

        #self.drop_down.grid()
    
    


    def popup(self, options):
        dialog = MyDialog(title="Login", parent=self.frame_content,options=options)
        return dialog.my_module, dialog.my_name, dialog.my_ip









class MyDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title, options):
        self.options = options
        self.my_name = None
        self.my_ip = None
        self.my_module = None
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

        return frame

    def ok_pressed(self):
        # print("ok")
        self.my_name = self.my_name_entry.get()
        self.my_ip = self.my_ip_entry.get()
        self.my_module = self.module.get()
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