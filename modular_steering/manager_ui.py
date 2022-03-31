
import tkinter as tk  # GUI toolkit
from PIL import Image, ImageTk  # GUI images
import os.path  # path operations
from platform import system  # returns the system/OS name
import time  # time access and conversions
import tkinter.messagebox

#constants
MQTT_ADDRESS = '192.168.1.104'
MQTT_TOPIC = 'test/message'

os.environ.__setitem__('DISPLAY', ':0.0')

class Manager_ui(tk.Tk):
    def __init__(self):
        super().__init__()  # call tk.Tk.__init__() to initialize tkinter object
        # window configuration
        self.configure(background="white")
        self.protocol("WM_DELETE_WINDOW", self.quit_popup)  # call self.quit_popup on exit button press
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
        self.labelframe_buttons = tk.LabelFrame(self.frame_content, text="", font=self.my_font,
                                                background="white")
        self.button_labelframe_1 = tk.Button(self.labelframe_buttons, text="quit", height=2, width=2,
                                             font=self.my_font, background=self.color_absolem_green_automation,
                                             command=self.button_1_callback)
        # --------------------------------------------------------------------------------------------------------------
        # canvas indicators
        width_canvas = 200
        height_canvas = 150
        indicator_diameter = 30
        padding = 10
        margin = 40
        xpadding_text = 80
        self.indicators = []
        self.indicators_text = []
        self.canvas_indicators = tk.Canvas(self.frame_content, width=width_canvas, height=height_canvas,
                                           background=self.color_absolem_grey)
        for count, value in enumerate(["indicator 1", "indicator 2", "indicator 3"]):
            self.indicators.append(
                self.canvas_indicators.create_oval(padding, padding + (count * margin), padding + indicator_diameter,
                                                   padding + (count * margin) + indicator_diameter))
            self.indicators_text.append(
                self.canvas_indicators.create_text(xpadding_text, padding + (count * margin) + (indicator_diameter / 2),
                                                   text=value, font=self.my_font))
      
        # call initialization class methods
        self.geometry_manager()

    def geometry_manager(self):
        """
        Control the application layout using tk.pack(), tk.place() and tk.grid()
        """
        # --------------------------------------------------------------------------------------------------------------
        # frames
        self.frame_content.pack(side="bottom", fill="both", expand=True, padx=5, pady=(0, 5))
        # --------------------------------------------------------------------------------------------------------------

        # labelframe with buttons
        self.labelframe_buttons.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.button_labelframe_1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------
    # button callbacks
    # ------------------------------------------------------------------------------------------------------------------
    def button_1_callback(self):
        #quit_popup()
        self.destroy()

    def quit_popup(self):
        """
        close program when "yes" is pressed
        """
        var = tk.messagebox.askyesno("Close program?", "Do you want to close the program?")
        if var:
            self.destroy()  # destroy all the widgets and exit mainloop


    # ------------------------------------------------------------------------------------------------------------------
    # print timestamp on other raspberry pi
    # ------------------------------------------------------------------------------------------------------------------
    def print_timestamp():
        publish.single(MQTT_TOPIC, payload=time.time(), qos=0, retain=False, hostname="192.168.1.104",
        port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None, transport="tcp")

    def stop(self):
        self.destroy()
#def main():
   # """
  #  Create an App() object and start the app
 #   """
 #   app = App()
#  app.mainloop()

