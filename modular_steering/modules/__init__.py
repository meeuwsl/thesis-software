import os
#from modular_steering.modules.temperaturemodule import TemperatureModule
#from modular_steering.modules.cameramodule import CameraModule

from .camera import CameraModule
from .temperature import TemperatureModule
from .linax import LinaxModule
from .printer import PrinterModule
from .adc import AdcModule
from .relay import RelayModule

#for module in os.listdir(os.path.dirname(__file__)):
#    if module == '__init__.py' or module[-3:] != '.py':
#        continue
#    __import__(module[:-3], locals(), globals())
#    print("imported something")
#del module