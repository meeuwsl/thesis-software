import module_a
import module_b
import module_gui
from multiprocessing import Process

import mqtt_client_abs

if __name__ == '__main__':
    a = Process(target=module_a.main, args=('a',))
    b = Process(target=module_b.main, args=('b',))
    gui = Process(target=module_gui.main, args=())
    

    #a.start()
    #b.start()
    gui.start()
    #a.join()
    #b.join()