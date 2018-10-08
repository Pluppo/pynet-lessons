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

net_conn = Netmiko(**R1)

output = net_conn.send_command('show ip arp', use_textfsm=True)

print()
print('-' * 80)
print(output)
print('-' * 80)
print()

net_conn.disconnect()
