import socket
import threading


def recv(udp_socket):  # 接受数据
    while True:
        recv_data = udp_socket.recvfrom(1024)  # 1024表示一次能接受的最大字节数
        # recv_data接收的数据是(数据,(发送方ip地址,端口号))
        recv_msg = recv_data[0]
        send_msg = recv_data[1]
        print((str(send_msg) + ':' + recv_msg.decode("gbk")))  # decode是解码 windows发送数据中文用的是gbk编码


def send(udp_socket, ip, port):  # 发送数据
    while True:
        send_data = input("请输入要发送的数据:")
        udp_socket.sendto(send_data.encode("utf-8"), (ip, port))


def main():
    """接发数据整体控制"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字
    udp_socket.bind(("", 6666))  # 绑定一个本地信息
    ip = input('请输入对方ip:')
    port = input('请输入对方端口号(另一个程序端口号为7777):')
    t_recv = threading.Thread(target=recv, args=(udp_socket,))  # 创建两个线程
    t_send = threading.Thread(target=send, args=(udp_socket, ip, int(port)))
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()