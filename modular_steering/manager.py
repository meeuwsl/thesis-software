from modular_steering.interface import ModuleInterface

class Manager:


    def register(self, module):
        #assert(issubclass(module.type(), ModuleInterface))
        #assert(isinstance(module, ModuleInterface))
        module.onstart()


    def unregister(self, module):
        pass
    
    def publish(topic, data):
        pass


