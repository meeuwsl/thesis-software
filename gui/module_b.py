import time

def main(input):
    a = 5
    while(a>0):
        print('this is process b')
        print(input)
        time.sleep(1)
        a -= 1