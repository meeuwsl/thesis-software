
import tkinter as tk  # GUI toolkit
from PIL import Image, ImageTk  # GUI images
import os.path  # path operations
from platform import system  # returns the system/OS name
import time  # time access and conversions
import tkinter.messagebox

os.environ.__setitem__('DISPLAY', ':0.0')

class Manager_ui(tk.Tk):
    def __init__(self):
        super().__init__()  # call tk.Tk.__init__() to initialize tkinter object
        
        # window configuration
        self.configure(background="white")
        self.attributes("-fullscreen", True) # full screen window
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
        # --------------------------------------------------------------------------------------------------------------
        # labelframe with buttons
        self.labelframe_quit = tk.LabelFrame(self.frame_content, text="quit", font=self.my_font,
                                                background="white")
        self.button_labelframe_quit = tk.Button(self.labelframe_quit, text="quit", height=2, width=2,
                                             font=self.my_font, background=self.color_absolem_green_automation,
                                             command=self.button_quit_callback)

        self.module1 = tk.LabelFrame(self.frame_content, text="module 1", font=self.my_font, background="white")
        self.b = tk.Button(self.module1, text = "module1", height = 2, width = 2)
      
        # call initialization class methods
        self.geometry_manager()

    def geometry_manager(self):
        """
        Control the application layout using tk.pack(), tk.place() and tk.grid()
        """
        # --------------------------------------------------------------------------------------------------------------
        # frames
        #self.frame_content.pack(side="bottom", fill="both", expand=True, padx=5, pady=(0, 5))
        self.frame_content.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------

        # labelframe with buttons
        self.labelframe_quit.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.button_labelframe_quit.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------


        # modules 
        self.module1.grid(row = 0, column = 1, padx=5, pady=5, sticky="nw")
        self.b.grid(row = 0, column = 1, padx=5, pady=5, sticky="nw")
    # button callbacks
    # ------------------------------------------------------------------------------------------------------------------
    def button_quit_callback(self):
        self.destroy()

    def stop(self):
        self.destroy()


    def add_module(self, module):
        module.grid(row = 0, column = 3, sticky = "nw", pady = 2)










                # --------------------------------------------------------------------------------------------------------------
        # canvas indicators
#        width_canvas = 200
#        height_canvas = 150
#        indicator_diameter = 30
#        padding = 10
#        margin = 40
#        xpadding_text = 80
#        self.indicators = []
#        self.indicators_text = []
#        self.canvas_indicators = tk.Canvas(self.frame_content, width=width_canvas, height=height_canvas,
#                                           background=self.color_absolem_grey)
#        for count, value in enumerate(["indicator 1", "indicator 2", "indicator 3"]):
#            self.indicators.append(
#                self.canvas_indicators.create_oval(padding, padding + (count * margin), padding + indicator_diameter,
#                                                   padding + (count * margin) + indicator_diameter))
#            self.indicators_text.append(
#                self.canvas_indicators.create_text(xpadding_text, padding + (count * margin) + (indicator_diameter / 2),
#                                                   text=value, font=self.my_font))