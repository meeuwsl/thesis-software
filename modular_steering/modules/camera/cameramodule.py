from modular_steering.interface import ModuleInterface

import tkinter as tk  # GUI toolkit

import json
import base64
import binascii

import time



class CameraModule(ModuleInterface):
    def __init__(self, mqttclient):
        super().__init__(mqttclient)
        print("cameramodule initialised")
        pass

    def onmsgrecv(self, message, payload):
        pass

    def onstop(self):
        print("stop cameramodule")
        pass
        
    def onstart(self):
        print("started cameramodule")
        while(1):
            time.sleep(3)
            print("cameramodule running..")

    def get_ui(self):
        return self.ui_frame
        #

    def block5(self):
        print("block5")
        self.send_test_message()

    def send_test_message(self):
        begin = time.time()

        name = self.entry_name_picture.get()
        msg = {"name":name, "begin" : begin}
        

        #with open("resources/logo.png", "rb") as image_file:
        with open("resources/bedroom-spa-suite.jpg", "rb") as image_file:
            data = binascii.b2a_base64(image_file.read()).decode()

        print("converted string type: ", type(data))
        # f=open("resources/logo.png", "rb") #3.7kiB in same folder
        # fileContent = f.read()
        # byteArr = bytearray(fileContent)
        # image = base64.decodestring(json.dumps(data)['image'])

        msg.update({ "picture": data })
        #print(msg)
        self.mqttclient.send("test/image", json.dumps(msg))
        end = time.time()