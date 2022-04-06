from modular_steering.interface import ModuleInterface

import tkinter as tk  # GUI toolkit


class CameraModule:
    def __init__(self, root):
        super().__init__()
        self.ui = tk.Button(text="camera", height=2, width=2)

        self.ui_frame = tk.Frame(root) 

        button4 = tk.Button(self.ui_frame, text ="Block4", fg ="orange") 
        button4.pack(side = tk.BOTTOM) 

        button5 = tk.Button(self.ui_frame, text ="Block5", fg ="orange", command=self.block5) 
        button5.pack(side = tk.BOTTOM) 

        button6 = tk.Button(self.ui_frame, text ="Block6", fg ="orange")
        button6.pack(side = tk.BOTTOM) 



        print("cameramodule initialised")
        pass

    def onmsgrecv(self, message, payload):
        pass

    def onstop(self):
        print("stop cameramodule")
        pass

    def onstart(self):
        print("start cameramodule")
        pass


    def get_ui(self):
        return self.ui_frame
        #

    def block5(self):
        print("block5")