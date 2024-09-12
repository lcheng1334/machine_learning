import socket
# 创建对象
socket_client = socket.socket()
# 连接服务器
socket_client.connect(("localhost", 8888))
while True:
    # 发送消息
    msg = input("请输入你要和服务端发送的消息: ")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))
    # 接受返回消息
    recv_data = socket_client.recv(1024)
    # 1024是缓冲区大小, 一般1024即可
    # recv是阻塞方法, 该代码不执行不会执行以下代码
    print(f"服务端回复的消息是: {recv_data.decode('UTF-8')}")
"""
encode: 将字符串格式编码成为字节
decode: 将字节解码成字符串
"""
socket_client.close()