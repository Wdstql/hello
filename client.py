from socket import *
import random
import time

ip='127.0.0.1' #服务器ip
host=12000 #端口号
address=(ip,host)
message = bytes('ping', encoding='utf-8') #报文内容
nums=10 #报文数
MAX_RTT=0 #最大RTT
MIN_RTT=2 #最小RTT，由于1秒即超时，则设初始值为2
SUM_RTT=0
packets=10 #成功接收的报文数

clientSocket=socket(AF_INET, SOCK_DGRAM) #创建套接字
clientSocket.settimeout(1) #设置1秒的等待时间

print('正在 Ping '+ip+'：')
for i in range(nums):
    start_time=time.time()
    clientSocket.sendto(message,address)
    print('来自'+ip+'的回复：',end='')
    try:
        _message,_address=clientSocket.recvfrom(1024)
    except:
        print('请求超时')
        packets-=1 #超时意味着丢包
        continue
    end_time=time.time()
    RTT=end_time-start_time #计算RTT
    print(bytes.decode(_message),'RTT=',RTT,'秒')
    if(RTT>MAX_RTT):
        MAX_RTT=RTT
    if(RTT<MIN_RTT):
        MIN_RTT=RTT
    SUM_RTT+=RTT
clientSocket.sendto(bytes('EXIT', encoding='utf-8'),address) #使服务器端退出

print(ip+' Ping 的统计信息：')
print('    数据包：已发送={0}, 已接收={1}, 丢包率={2}%'.format(nums,packets,(nums-packets)*100/nums))
if packets>0:
    print('往返行程的估计时间(以秒为单位):')
    print('    最短={0}s, 最长={1}s, 平均={2}秒'.format(MIN_RTT,MAX_RTT,SUM_RTT/packets))
else:
    print('所有数据包均已丢失，不计算RRT')


