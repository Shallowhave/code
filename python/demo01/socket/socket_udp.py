# encoding = 'utf-8'
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 9999)
# data = input('请输入要发送的信息：')
data = ('你好')

s.sendto(data.encode('utf-8'), addr)
s.close()
