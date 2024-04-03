from ipaddress import *
ip = ip_address('111.24.160.159')
net = ip_address('111.24.160.128')
ip = f'{ip:b}'
net = f'{net:b}'
for i in range(32):
    if ip[i] == '1' and net[i] == '0':
        print(i - 1)
        break