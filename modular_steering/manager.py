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
        self.manager_ui = Manager_ui(master_obj=self, root_=self.root)
        print("manager_ui initialised")
        self.control_ui = Control_ui(master_obj=self, root_=self.root)
        print("control_ui initialised")

        self.mqtt_client = MqttClient(broker_address, self.on_message)
        
        self.registered_modules = {}
        self.available_modules_dict = {}
        self.available_modules_arr = []

        self.locations = {
            0 : (0,0),
            1 : (0,1),
            2 : (0,2),
            3 : (0,3),
            4 : (1,0),
            5 : (1,1),
            6 : (1,2),
            7 : (1,3),
            8 : (1,4),
        }

        for (key, value) in globals().items():
            if key[-6:] == "Module":
                #print(key + "aanwezig")
                self.available_modules_arr.append(key)
                self.available_modules_dict.update({key : value})
                print(value)

        self.manager_ui.options1 = self.available_modules_arr

        self.manager_ui.set_optional_modules(self.available_modules_arr)
        print("modules set")

        print("before")
        print("after")


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
        print("extra line------------------------------------------------")
        print("available modules: ", self.available_modules_arr)
        

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
        #self.control_ui = Control_ui(self)

        #gui = Process(target=self.ui.mainloop(), args=())
        #self.manager_ui.mainloop()
        #self.control_ui.mainloop()
        print("ui started")
        
        #gui.start()
        #gui.join()
        
        
        
        #self.manager_ui.root.mainloop()
        print("between")
        self.control_ui.root.mainloop()
        print("done with run")


    def stop(self):
        self.manager_ui.stop()


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


    def add_module(self, wanted_module, wanted_name, wanted_ip, wanted_location):
        wanted_class = self.available_modules_dict.get(wanted_module)
        print("location int in manager: ", wanted_location)
        print("location in manager: ", self.locations.get(wanted_location))
        instance = wanted_class(self.control_ui.frames.get(self.locations.get(wanted_location)), self.mqtt_client)
        print("instance :" , instance)
        self.control_ui.add_module_ui(instance.get_ui(), self.locations.get(wanted_location))
        #self.add_module(instance)
        self.registered_modules[wanted_name] = instance
        pass


    def remove_module(self, wanted_module):
        self.manager_ui.remove_ui(self.registered_modules.get(wanted_module))
        self.registered_modules.pop(wanted_module)
