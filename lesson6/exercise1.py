#!/usr/bin/env python3.6

from netmiko import Netmiko
from getpass import getpass

R1 = {
    'host': '192.168.0.51',
    'username': 'pluppo',
    'password': getpass(),
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**R1)

print(net_conn.find_prompt())
