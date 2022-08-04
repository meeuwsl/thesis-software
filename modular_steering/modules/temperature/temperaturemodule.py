from modular_steering.interface import ModuleInterface

import tkinter as tk  # GUI toolkit
import time


class TemperatureModule(ModuleInterface):
    def __init__(self, mqttclient):
        super().__init__(mqttclient)
        print("Temperature module initialised")
        pass


    def onmsgrecv(self, path: str, file_name: str) -> str:
        pass

    def onstop(self, full_file_path: str) -> dict:
        pass
    
    def onstart(self):
        print("started temperaturemodule")
        while(1):
            time.sleep(3)
            print("temperaturemodule running..")

    def get_ui(self):
        return self.ui_frame
        pass
