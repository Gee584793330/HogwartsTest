import threading

n=0

lock= threading.Lock()

def task():
    global n
    lock.acquire()
    for i in range(1000000):
        n+=1
    print(f"当前task中n的值是{n}")
    lock.release()

def task1():
    global n
    lock.acquire()

    for i in range(1000000):
        n += 1

    print(f"当前task1中n的值是{n}")
    lock.release()

if __name__ == '__main__':
    th1=threading.Thread(target=task)
    th2=threading.Thread(target=task1)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f"最后n的值为{n}")
