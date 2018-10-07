#!/usr/local/bin/python3.6

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

output = net_conn.send_config_set('snmp-server community cisco123')

print()
print('-' * 80)
print(output)
print('-' * 80)
print()

output = net_conn.send_config_from_file('file_commands.txt')

print()
print('-' * 80)
print(output)
print('-' * 80)
print()

output = net_conn.send_command('show run | inc snmp-server')

print()
print('-' * 80)
print(output)
print('-' * 80)
print()

output = net_conn.send_command('show run | inc ntp')

print()
print('-' * 80)
print(output)
print('-' * 80)
print()

net_conn.disconnect()
