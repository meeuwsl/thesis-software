from modular_steering.modules.cameramodule import CameraModule
from modular_steering.modules.temperaturemodule import TemperatureModule
from modular_steering.interface import ModuleInterface

def test_a():
    assert(True)

def test_moduleimplementation1():
    assert(issubclass(CameraModule, ModuleInterface))

def test_moduleimplementation2():
    assert(not (issubclass(TemperatureModule, ModuleInterface)))
