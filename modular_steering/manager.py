from modular_steering.mqttclient import MqttClient
from modular_steering.interface import ModuleInterface
from modular_steering.manager_ui import Manager_ui
from modular_steering.control_ui import Control_ui

from multiprocessing import Process

from modular_steering.modules import * 

import tkinter as tk  # GUI toolkit

import json
import base64
import binascii

import time

class Manager:
    def __init__(self, broker_address):
        self.root = tk.Tk()
        self.ui = Manager_ui(self.root, self)

        self.mqtt_client = MqttClient(broker_address, self.on_message)
        
        self.registered_modules = {}
        self.available_modules = []
        self.available_modules1 = {}

        for (key, value) in globals().items():
            if key[-6:] == "Module":
                #print(key + "aanwezig")
                self.available_modules.append(key)
                self.available_modules1.update({key : value})
                print(value)

        self.ui.options1 = self.available_modules1

        self.ui.set_optional_modules(self.available_modules)

        pass



    def register(self, module):
        module.onstart()
        self.registered_modules.append(module)
        print(self.registered_modules)
        pass


    def unregister(self, module):
        pass
    
    def publish(topic, data):
        pass


    def run(self):
        print("available modules: ", self.available_modules)
        

        #ask what modules one wants to use in this setup
        #print("specify what modules do you want: ", end="")
        #wanted_modules = input().split()
        #wanted_modules = []
  

        # output
        #print(wanted_modules)
        

        #print("wanted modules: ", wanted_modules)

        
        #register wanted modules
        # for m in wanted_modules:
        #     wanted_class = globals()[ m + "Module"]
        #     instance = wanted_class(self.ui.frame_content)
        #     self.register(instance)
        #     self.ui.add_module(instance.get_ui())


        topics = []
        topics.append("test/message")
        topics.append("test/test")
        topics.append("test/image")

        #start mqtt_client
        self.mqtt_client.start(topics)


#        module = CameraModule()
#        fake_module = TemperatureModule()

#        self.register(module)
        print("done")
#        self.register(fake_module)
        self.control_ui = Control_ui(self)

        #gui = Process(target=self.ui.mainloop(), args=())
        self.ui.mainloop()
        print("ui started")
        
        #gui.start()
        #gui.join()

    def stop(self):
        self.ui.stop()


    def on_message(self, message):
        #print("manager: received message from mqtt: ", message.payload)
        

        if(message.topic == "test/image"):
            #print ("Topic : ", message.topic)
            msg_dict = json.loads(message.payload)
            picture_name = msg_dict.get("name")
            picture_content = msg_dict.get("picture")
            #print("in manager type of picture content: ", type(picture_content))
            picture_filename = "tmp/" + "name_" + picture_name + ".jpg"
            f = open(picture_filename, "wb")  #there is a output.jpg which is different
            f.write(binascii.a2b_base64(picture_content))
            f.close()
            begin = msg_dict.get("begin")
            end = time.time()
            print("sending + receiving took: ", end-begin)


        pass

    def test1(self):
        print("method from manager executed")


    def add_module(self, wanted_module, wanted_name, wanted_ip):
        wanted_class = self.available_modules1.get(wanted_module)
        instance = wanted_class(self.ui.frame_content, self.mqtt_client)
        print("instance :" , instance)
        self.ui.add_module(instance.get_ui())
        #self.add_module(instance)
        self.registered_modules[wanted_name] = instance
        pass


    def remove_module(self, wanted_module):
        self.ui.remove_ui(self.registered_modules.get(wanted_module))
        self.registered_modules.pop(wanted_module)
