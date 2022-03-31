available_modules = []

from modular_steering.mqttclient import MqttClient

from modular_steering.interface import ModuleInterface
from multiprocessing import Process

from modular_steering.modules.cameramodule import CameraModule
available_modules.append("Camera")

from modular_steering.modules.temperaturemodule import TemperatureModule
available_modules.append("Temperature")

from modular_steering.manager_ui import Manager_ui





class Manager:

    def __init__(self, broker_address):
        self.registered_modules = []
        self.ui = Manager_ui()
        self.mqtt_client = MqttClient(broker_address, self.on_message)
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
        print("available modules: ", available_modules)
        #ask what modules one wants to use in this setup
        print("specify what modules do you want: ", end="")
        wanted_modules = input().split()
  
        # output
        print(wanted_modules)
        

        print("wanted modules: ", wanted_modules)

        
        #register wanted modules
        for m in wanted_modules:
            wanted_class = globals()[m + "Module"]
            instance = wanted_class()
            self.register(instance)


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