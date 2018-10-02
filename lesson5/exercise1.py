#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

def ssh_con(ip_addr, username, password):
    print()
    print('{:10} {:10}'.format('IP address:', ip_addr))
    print('{:10} {:10}'.format('Username:', username))
    print('{:10} {:10}'.format('Password:', password))
    print()

ssh_con('10.0.0.1', 'user1', 'password 123')
ssh_con(username='user2', password='password234', ip_addr='10.0.0.2')
ssh_con('10.0.0.3', password='password345', username='user3')

def ssh_con2(ip_addr, username, password, device_type='cisco_ios'):
    print()
    print('{:10} {:10}'.format('IP address:', ip_addr))
    print('{:10} {:10}'.format('Username:', username))
    print('{:10} {:10}'.format('Password:', password))
    print('{:10} {:10}'.format('Device:', device_type))
    print()

ssh_con2('192.168.0.1', 'user21', 'password321', 'junos')
ssh_con2('192.168.0.2', 'user22', 'password322')

my_dict = {
    'ip_addr': '192.168.0.3',
    'username': 'user23',
    'password': 'password323',
    'device_type': 'fortios'
}

ssh_con2(**my_dict)
