#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

net_device = {'ip_addr': '192.168.0.1', 'vendor': 'cisco', 'username': 'admin', 'password': '123456'}

print(net_device['ip_addr'])
print()

if net_device['vendor'] == 'cisco':
    net_device.update({'platform': 'ios'})
elif net_device['vendor'] == 'juniper':
    net_device.update({'platform': 'junos'})

bgp_fields = {'bgp_as': '65001', 'peer_as': '65555', 'peer_ip': '88.99.88.99'}

net_device.update(bgp_fields)

for key in net_device:
    print(key)

print()
for key, value in net_device.items():
    print("{:<10}{:<10}".format(key, value))
