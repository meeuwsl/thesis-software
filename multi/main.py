import sub_a
import sub_b

from multiprocessing import Process



if __name__ == '__main__':
    a = Process(target=sub_a.process_a, args=('a',))
    b = Process(target=sub_b.process_b, args=('b',))

    a.start()
    b.start()
    a.join()
    b.join()