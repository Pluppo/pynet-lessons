#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline
import os

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []

for host in range(1,255):
    ip_list.append('192.168.0.' + str(host))

for index, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(index, ip_addr))

new_list = ip_list[100:105]

for ip in new_list:
    print('-' * 60)
    os.system(base_cmd + ' ' + ip)
    print('-' * 60)
