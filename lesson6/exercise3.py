#!/usr/bin/env python3.6

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()

R1 = {
    'host': '192.168.0.51',
    'username': 'pluppo',
    'password': password,
    'device_type': 'cisco_ios'
}

filename = 'test'
command = 'delete unix:{}'.format(filename)

net_conn = Netmiko(**R1)

output = net_conn.send_command_timing(command)

if 'Delete filename' in output:
    output += net_conn.send_command_timing('\n')

if 'confirm' in output:
    output += net_conn.send_command_timing('\n')

net_conn.disconnect()

print()
print('-' * 80)
print(output)
print('-' * 80)
print()
