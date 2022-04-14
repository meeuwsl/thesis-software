from modular_steering.interface import ModuleInterface

import tkinter as tk  # GUI toolkit

import json
import base64
import binascii

import time



class RelayModule(ModuleInterface):
    def __init__(self, root, mqttclient):
        super().__init__(mqttclient)

        self.ui_frame = tk.Frame(root) 

        print("LinaxModule initialised")
        pass

    def onmsgrecv(self, message, payload):
        pass

    def onstop(self):
        print("stop LinaxModule")
        pass

    def onstart(self):
        print("start LinaxModule")
        pass


    def get_ui(self):
        return self.ui_frame
        #

    def block5(self):
        print("block5")
        self.send_test_message()

    def send_test_message(self):
        pass