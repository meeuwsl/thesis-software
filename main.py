
from modular_steering.modules.cameramodule import CameraModule
from modular_steering.modules.temperaturemodule import TemperatureModule
from modular_steering.interface import ModuleInterface
from modular_steering.manager import Manager


def test_manager():
    assert(True)
    
    manager = Manager("192.168.1.104")
    manager.run()







test_manager()