import threading
from time import sleep


def downlaod(n):
    images = ['girl.jpg', 'boy.jpg', 'mam.jpg']
    for image in images:
        print("正在下载：", image)
        sleep(n)
        print("下载成功过", format(image))


def listenMusic():
    musics = ['music1', 'music2', 'music3']
    for music in musics:
        sleep(0.5)
        print("正在听",format(music))


if __name__ == "__main__":
    t = threading.Thread(target=downlaod, name='aa', args=(1,))
    t.start()

    t1 = threading.Thread(target=listenMusic, name='aa')
    t1.start()

    # n=1
    # while True:
    #     print(n)
    #     sleep(1.5)
    #     n+=1
