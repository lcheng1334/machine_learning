""""""
import threading
import time

"""
进程: 程序在操作系统内运行, 即为一个运行进程(公司)
线程: 进程内部有多个线程, 程序运行的本质是由进程内部的线程在实际工作(公司员工工作)
并行执行:
    1. 多个进程在同时运行，即不同的程序同时运行，称为: 多任务并行执行(任务管理器)
    2. 一个进程内的多个线程同时运行, 被称为: 多线程并行执行(公司的员工上班, 各司其职)
"""

def sing():
    while True:
        print("唱歌")
        time.sleep(1)

def dance():
    while True:
        print("跳舞")
        time.sleep(1)
# 单线程, 完成一个线程才能执行下一个线程

def sing_msg(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance_msg(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # sing()
    # dance()
    """多线程, 多个线程一起执行"""
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    """启动多线程"""
    # sing_thread.start()
    # dance_thread.start()
    """
    使用msg对任务进行传参, 传参可以使用元组和字典方式
    """
    # 使用元组时, 仅有一个对象一定要加上"," TODO: (a,) √    (a) ×
    sing_msg_thread = threading.Thread(target=sing_msg, args=("我要唱歌", ))
    # k值为参数, v值为内容
    dance_msg_thread = threading.Thread(target=dance_msg, kwargs={"msg": "我在跳舞"})
    sing_msg_thread.start()
    dance_msg_thread.start()