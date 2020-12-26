import threading
from time import sleep

ticket=1000

def run1():
    global ticket
    for i in range(100):
        # sleep(0.1)
        ticket-=1
        print(i)


# def run2():
#     global money
#     for i in range(1000):
#         money-=1

if __name__ == '__main__':
    th1=threading.Thread(target=run1(),name="th1")
    th2=threading.Thread(target=run1(),name="th2")
    th3=threading.Thread(target=run1(),name="th3")
    th4=threading.Thread(target=run1(),name="th4")

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print("ticket",ticket)
