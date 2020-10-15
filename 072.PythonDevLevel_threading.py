import threading


class MyThread(threading.Thread):
    def run(self):
        global n
        lock.acquire()
        n += 1
        lock.release()
        print(self.name + ' set n to ' + str(n))


n = 0
lock = threading.Lock()

if __name__ == '__main__':

    for i in range(5):
        t = MyThread()
        t.start()

    print('final num: %d' % n)
"""
Thread-1 set n to 1
Thread-2 set n to 2
Thread-3 set n to 3
Thread-4 set n to 4
Thread-5 set n to 5
final num: 5
"""
