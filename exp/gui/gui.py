
import tkinter as tk  # GUI toolkit
from PIL import Image, ImageTk  # GUI images
import os.path  # path operations
from platform import system  # returns the system/OS name
import time  # time access and conversions
from datetime import datetime  # manipulating dates and times
import matplotlib  # visualizations
from matplotlib import pyplot as plt  # general plotting
from matplotlib import animation  # live plot animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # embedding plot in tkinter
import paho.mqtt.publish as publish


#constants
MQTT_ADDRESS = '192.168.1.104'
MQTT_TOPIC = 'test/message'

os.environ.__setitem__('DISPLAY', ':0.0')

class App(tk.Tk):
    def __init__(self):
        super().__init__()  # call tk.Tk.__init__() to initialize tkinter object
        # --------------------------------------------------------------------------------------------------------------
        # detect system/OS
        if system() == "Linux":
            self.is_linux = True
        else:
            self.is_linux = False
        # --------------------------------------------------------------------------------------------------------------
        # get program path and desktop path
        self.path = os.path.dirname(os.path.realpath(__file__))  # path to .py file
        if self.is_linux:  # path to desktop
            self.path_desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        else:
            self.path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # --------------------------------------------------------------------------------------------------------------
        # window configuration
        self.title("Absolem GUI template")
        if not self.is_linux:
            self.iconbitmap(self.path + "/resources/favicon.ico")  # set favicon (doesn't work on Linux)
        self.geometry("1280x720+0+0")  # set window dimensions
        self.configure(background="white")
        self.protocol("WM_DELETE_WINDOW", self.quit_popup)  # call self.quit_popup on exit button press
        self.attributes("-fullscreen", True) # full screen window
        # self.configure(cursor="none") # no cursor for touchscreens

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
        self.frame_header = tk.Frame(self, background=self.color_absolem_grey)
        self.frame_content = tk.Frame(self, background="white")
        # --------------------------------------------------------------------------------------------------------------
        # logo and title
        self.logo_butterfly = ImageTk.PhotoImage(Image.open(self.path + "/resources/logo_butterfly.png"))
        self.label_logo_butterfly = tk.Label(self.frame_header, image=self.logo_butterfly,
                                             background=self.color_absolem_grey)
        self.logo = ImageTk.PhotoImage(Image.open(self.path + "/resources/logo.png"))
        self.label_logo = tk.Label(self.frame_header, image=self.logo, background=self.color_absolem_grey)
        self.label_title = tk.Label(self.frame_header, text="Title placeholder", background=self.color_absolem_grey,
                                    font=self.my_font_title)
        # --------------------------------------------------------------------------------------------------------------
        # buttons
        self.button_1 = tk.Button(self.frame_content, text="Button 1", height=2, width=20, font=self.my_font,
                                  background=self.color_absolem_green, command=self.button_1_callback)
        self.button_2 = tk.Button(self.frame_content, text="Button 2", height=2, width=20, font=self.my_font,
                                  background=self.color_absolem_lightblue, command=self.button_2_callback)
        self.button_3 = tk.Button(self.frame_content, text="Button 3", height=2, width=20, font=self.my_font,
                                  background=self.color_absolem_darkblue, foreground="white",
                                  command=self.button_3_callback)
        # --------------------------------------------------------------------------------------------------------------
        # labelframe with buttons
        self.labelframe_buttons = tk.LabelFrame(self.frame_content, text="Labelframe with buttons", font=self.my_font,
                                                background="white")
        self.button_labelframe_1 = tk.Button(self.labelframe_buttons, text="Button 1", height=2, width=20,
                                             font=self.my_font, background=self.color_absolem_green_automation,
                                             command=self.button_labelframe_1_cb)
        self.button_labelframe_2 = tk.Button(self.labelframe_buttons, text="Button 2", height=2, width=20,
                                             font=self.my_font, background=self.color_absolem_blue_innovation,
                                             command=self.button_labelframe_2_cb)
        self.button_labelframe_3 = tk.Button(self.labelframe_buttons, text="Button 3", height=2, width=20,
                                             font=self.my_font, background=self.color_absolem_blue_industry,
                                             command=self.button_labelframe_3_cb)
        # --------------------------------------------------------------------------------------------------------------
        # labels
        self.label_1 = tk.Label(self.frame_content, text="Static label", font=self.my_font, height=2, width=30,
                                background="white")
        self.label_2 = tk.Label(self.frame_content, text="Static label with border", font=self.my_font, height=2,
                                width=30, background="white", borderwidth=2, relief="groove")
        self.label_3_var = tk.StringVar()
        self.label_3_var.set("Dynamic label (press button 1)")
        self.label_3 = tk.Label(self.frame_content, textvariable=self.label_3_var, font=self.my_font, height=2,
                                width=30, background="white")
        # --------------------------------------------------------------------------------------------------------------
        # entry
        self.entry_1_var = tk.DoubleVar()
        self.entry_1 = tk.Entry(self.frame_content, textvariable=self.entry_1_var, font=self.my_font,
                                background="white", cursor="xterm")
        self.entry_2_var = tk.IntVar()
        self.entry_2 = tk.Entry(self.frame_content, textvariable=self.entry_2_var, font=self.my_font,
                                background="white", cursor="xterm")
        # --------------------------------------------------------------------------------------------------------------
        # checkbox
        self.checkbox_1_boolean = tk.BooleanVar()
        self.checkbox_1 = tk.Checkbutton(self.frame_content, text="Checkbox", variable=self.checkbox_1_boolean,
                                         onvalue=True, offvalue=False, font=self.my_font, background="white",
                                         activebackground="white")
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
        # --------------------------------------------------------------------------------------------------------------
        # live plot
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot()  # axes contains the figure elements (Axis, Tick, Line2D ...)
        self.line = self.axes.plot()  # create empty Line2D object
        self.canvas_plot = FigureCanvasTkAgg(self.figure, self.frame_content).get_tk_widget()
        # animate figure by calling self.plot_animate every [interval] ms
        self.animation = animation.FuncAnimation(self.figure, self.plot_animate, interval=1000)
        # --------------------------------------------------------------------------------------------------------------
        # call initialization class methods
        self.plot_formatting()
        self.geometry_manager()

    def geometry_manager(self):
        """
        Control the application layout using tk.pack(), tk.place() and tk.grid()
        """
        # --------------------------------------------------------------------------------------------------------------
        # frames
        self.frame_header.pack(side="top", fill="x", expand=False, padx=5, pady=(5, 0))
        self.frame_content.pack(side="bottom", fill="both", expand=True, padx=5, pady=(0, 5))
        # --------------------------------------------------------------------------------------------------------------
        # logo and title in frame_header
        self.label_logo_butterfly.grid(row=0, column=0, sticky="w")
        self.label_logo.grid(row=0, column=1, padx=(5, 0), sticky="w")
        self.label_title.grid(row=0, column=2, padx=30, sticky="w")
        self.label_title.place(relx=0.5, rely=0.5, anchor="center")  # place in center of the window
        # --------------------------------------------------------------------------------------------------------------
        # buttons
        self.button_1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.button_2.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.button_3.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
        #self.button_4.grid(row=6, column=0, padx=5, pady=5, sticky="nw")

        # --------------------------------------------------------------------------------------------------------------
        # labelframe with buttons
        self.labelframe_buttons.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
        self.button_labelframe_1.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.button_labelframe_2.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.button_labelframe_3.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------
        # labels
        self.label_1.grid(row=4, column=0, padx=5, pady=5, sticky="nw")
        self.label_2.grid(row=5, column=0, padx=5, pady=5, sticky="nw")
        self.label_3.grid(row=6, column=0, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------
        # entry
        self.entry_1.grid(row=0, column=1, padx=5, pady=5, sticky="nw")
        self.entry_2.grid(row=1, column=1, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------
        # checkbox
        self.checkbox_1.grid(row=2, column=1, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------
        # canvas indicators
        self.canvas_indicators.grid(row=3, column=1, rowspan=3, padx=5, pady=5, sticky="nw")
        # --------------------------------------------------------------------------------------------------------------
        # canvas plot
        self.canvas_plot.grid(row=0, column=2, rowspan=7, sticky="s")

    # ------------------------------------------------------------------------------------------------------------------
    # button callbacks
    # ------------------------------------------------------------------------------------------------------------------
    def button_1_callback(self):
        """
        called on button_1 press
            set label_3 to a random integer between 0 and 100
        """
        self.label_3_var.set(self.getTemp())
        pass

    def button_2_callback(self):
        print_timestamp()
#         """
#         called on button_2 press
#             popup a messagebox and set indicator 1
#         """
#         var = messagebox.askyesno("Title", "Question?")
#         if var:
#             self.canvas_indicators.itemconfig(self.indicators[0], fill="red")
#         else:
#             self.canvas_indicators.itemconfig(self.indicators[0], fill="")

    def button_3_callback(self):
        """
        called on button_3 press
            save plot on desktop as png with timestamp as filename and showinfo
        """
        timestamp = self.get_timestamp("%Y-%m-%d_%H-%M-%S")
        file_name = self.path_desktop + "/" + timestamp + ".png"
        plt.savefig(file_name)
        self.showinfo_popup(title="Saved as png", message=f"Saved @ {file_name}")

    def button_labelframe_1_cb(self):
        """
        called on button_labelframe_1 press
        """
        pass

    def button_labelframe_2_cb(self):
        """
        called on button_labelframe_2 press
        """
        pass

    def button_labelframe_3_cb(self):
        """
        called on button_labelframe_3 press
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # popup callbacks
    # ------------------------------------------------------------------------------------------------------------------
    def quit_popup(self):
        """
        close program when "yes" is pressed
        """
        var = messagebox.askyesno("Close program?", "Do you want to close the program?")
        if var:
            self.destroy()  # destroy all the widgets and exit mainloop

    @staticmethod
    def showinfo_popup(title, message):
        """
        call messagebox.showinfo
            (static method cannot access the class attributes or instance attributes)
        @param title: string
        @param message: string
        """
        messagebox.showinfo(title, message)

    # ------------------------------------------------------------------------------------------------------------------
    # live plot
    # ------------------------------------------------------------------------------------------------------------------
    def plot_animate(self, *args):
        """
        called by animation.FuncAnimation() every [interval] milliseconds; refresh plot
        """
        x_data, y_data = [], []
        for i in range(10):  # get plot data
            x_data.append(random.randint(0, 100))
            y_data.append(random.randint(0, 100))
        if self.line:  # clear current line on plot
            self.line.remove()
        self.line, = self.axes.plot(x_data, y_data, color=self.color_absolem_darkblue,
                                    label="Line 1")  # create new line
        plt.legend(loc="upper right")  # refresh legend for new line

    def plot_formatting(self):
        """
        plot format settings
            called once at initialization
        """
        plt.grid(True)
        plt.title("Plot title")
        plt.xlabel("x label")
        plt.ylabel("y label")
        plt.style.use("fivethirtyeight")
        self.axes.set_xlim(left=0, right=100)
        self.axes.set_ylim(bottom=0, top=100)

    # ------------------------------------------------------------------------------------------------------------------
    # get timestamp
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_timestamp(frmt="%Y-%m-%d %H:%M:%S"):
        """
        get current date and time, formatted according to frmt
        @param frmt: format string
        """
        return (datetime.now()).strftime(frmt)

    # ------------------------------------------------------------------------------------------------------------------
    # get temp
    # ------------------------------------------------------------------------------------------------------------------

    def getTemp(self):
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D18)
        cs.direction = digitalio.Direction.OUTPUT
        thermocouple = adafruit_max31856.MAX31856(spi, cs)
        return thermocouple.temperature
    
    
    # ------------------------------------------------------------------------------------------------------------------
    # print timestamp on other raspberry pi
    # ------------------------------------------------------------------------------------------------------------------

def print_timestamp():
    publish.single(MQTT_TOPIC, payload=time.time(), qos=0, retain=False, hostname="192.168.1.104",
    port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None, transport="tcp")

def start():
    """
    Create an App() object and start the app
    """
#    print(hello)
    app = App()
    app.mainloop()

