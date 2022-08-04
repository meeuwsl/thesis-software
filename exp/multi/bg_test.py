import sys
import time
from datetime import datetime



if __name__ == "__main__":
    file_object = open('bg_test.txt', 'a',buffering=1)
    a = 20
    while(a>0):
        file_object.write('hello' +  datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        file_object.flush()
        time.sleep(5)
        a = a - 1
       
    file_object.close()
    
