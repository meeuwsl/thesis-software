from modular_steering.modules.cameramodule import CameraModule
from modular_steering.modules.temperaturemodule import TemperatureModule
from modular_steering.interface import ModuleInterface
from modular_steering.manager import Manager

manager = Manager()
module = CameraModule()
fake_module = TemperatureModule()

manager.register(module)
manager.register(fake_module)

