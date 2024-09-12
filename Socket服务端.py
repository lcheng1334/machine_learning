""""""
import socket

"""
Socket: 进程通信的一个工具
Socket服务端: 等待进程连接, 接受发来的消息和回复消息(被动)
Socket客户端: 主动连接服务端, 可以发送和接受消息(主动)
"""

# 创建socket对象
socket_server = socket.socket()
# 绑定socket_server到指定IP和地址
socket_server.bind(("localhost", 8888))
# 服务器开始监听端口
socket_server.listen(1)
# listen方法接受的参数为, 接受的客户端连接数量
# 等待接受客户端连接, 获得连接对象
# result: tuple = socket_server.accept()
# conn = result[0] # 客户端和服务器的连接对象
# address = result[1] # 客户端的地址连接
conn, address = socket_server.accept()
# accept方法返回二元元组(连接对象, 客户端地址信息)
# accept方法是一种阻塞的方法, 如果没有客户端连接则会停止运行下面的代码
print(f"接受到客户端连接, 客户端的信息是{address}")

while True:
    # 接受客户端信息, 使用客户端和服务端的连接对象, 不是socket_server
    data: str = conn.recv(1024).decode("UTF-8") # receive
    # recv方法接受的参数是缓冲区大小, 一般是1024
    # recv方法返回值是一个字节数组也是bytes对象, 不是字符串
    # decode方法使用UTF-8编码可以将字节数组转换成字符串对象
    print(f"客户端发送的消息是: {data}")

    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息: ")
    if msg == "exit":
        break
    # encode方法使用UTF-8编码将字符串对象转换成字节对象
    conn.send(msg.encode("UTF-8"))

# 关闭
conn.close()
socket_server.close()