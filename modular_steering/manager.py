from modular_steering.mqttclient import MqttClient
from modular_steering.interface import ModuleInterface
from modular_steering.manager_ui import Manager_ui

from multiprocessing import Process

from modular_steering.modules import * 

import tkinter as tk  # GUI toolkit




class Manager:
    def __init__(self, broker_address):
        self.registered_modules = []
        self.root = tk.Tk()
        self.ui = Manager_ui(self.root, self)
        self.mqtt_client = MqttClient(broker_address, self.on_message)
        
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
        wanted_modules = []
  

        # output
        print(wanted_modules)
        

        #print("wanted modules: ", wanted_modules)

        
        #register wanted modules
        for m in wanted_modules:
            wanted_class = globals()[ m + "Module"]
            instance = wanted_class(self.ui.frame_content)
            self.register(instance)
            self.ui.add_module(instance.get_ui())


        topics = []
        topics.append("test/message")

        #start mqtt_client
        self.mqtt_client.start(topics)


#        module = CameraModule()
#        fake_module = TemperatureModule()

#        self.register(module)
        print("done")
#        self.register(fake_module)

        #gui = Process(target=self.ui.mainloop(), args=())
        self.ui.mainloop()
        #gui.start()
        #gui.join()

    def stop(self):
        self.ui.stop()


    def on_message(payload):
        print("received message from mqtt: ", payload)
        pass

    def test1(self):
        print("method from manager executed")