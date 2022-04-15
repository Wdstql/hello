from socket import *
import random

serverSocket=socket(AF_INET, SOCK_DGRAM) #创建套接字
serverSocket.bind(('127.0.0.1',12000)) #绑定ip和端口
print('Waiting for connection...')

while True:
    message,address=serverSocket.recvfrom(1024) #接收报文
    _message=bytes.decode(message)
    print('接收到来自{0}的信息：{1}'.format(address,_message))
    if _message=='EXIT': #设置服务器退出命令
        print('bye-bye')
        break
    rand=random.randint(1,10)
    if rand<4: #30%数据丢失
        continue
    serverSocket.sendto(bytes('pong', encoding='utf-8'),address)
serverSocket.close()



