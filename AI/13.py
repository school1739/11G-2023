'''from ipaddress import *

net = ip_network('217.9.191.133/255.255.192.0', 0)
for ip in net:
    if bin(int(ip)).count('1') % 2 == 0:
        k += 1
print(net)'''
'''
from ipaddress import *
k = 0
for i in range(32):
    net = ip_network('71.192.0.12/'+ str(i), 0)
    sub = tr(net).split('/')
    if sub[0]== '71.192.0.0':
        k += 1
print(k)'''