
#import modular_steering.modules 
#from modular_steering.modules.cameramodule import CameraModule
#from modular_steering.modules.temperaturemodule import TemperatureModule
#from modular_steering.interface import ModuleInterface
import socket
import json
from modular_steering.manager import Manager


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip



def main():

    #get ip of this device
    ip = get_ip()
    print(type(ip))

    #load conf data
    conf_file = open("config.json")
    conf_data = json.load(conf_file)

    #init namager with ip of this device
    manager = Manager(ip, conf_data, ip)

    #run
    manager.run()


if __name__ == '__main__':
    main()