#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
import readline

ip_list = ['192.168.10.1', '192.168.20.1', '192.168.30.1', '192.168.40.1', '192.168.50.1']

ip_list.append('10.0.0.1')

ip_list.extend(('172.16.1.1', '172.16.2.1'))

print(ip_list)
print(ip_list[0])
print(ip_list[-1])

ip_list.pop(0)
ip_list.pop(-1)

ip_list[0] = '2.2.2.2'

print(ip_list[0])
