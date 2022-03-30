from modular_steering.interface import ModuleInterface
from multiprocessing import Process

from modular_steering.manager_ui import Manager_ui

class Manager:
    def __init__(self):
        self.registered_modules = []
        self.ui = Manager_ui()
        pass

    def register(self, module):
        module.onstart()
        self.registered_modules.append(module)
        print(self.registered_modules)
        


    def unregister(self, module):
        pass
    
    def publish(topic, data):
        pass


    def run(self):
        #gui = Process(target=self.ui.mainloop(), args=())
        self.ui.mainloop()
        #gui.start()
        #gui.join()

    def stop(self):
        self.ui.stop()