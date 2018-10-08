#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

with open("show_arp.txt") as f:
    show_arp = f.read()

found1, found2 = (False, False)

print()
for line in show_arp.splitlines():
    if not 'Internet' in line:
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if ip_addr == '10.220.88.1':
        print("Default gateway IP/Mac is: {}/{}".format(ip_addr, mac_addr))
        found1 = True
    elif ip_addr == '10.220.88.30':
        print(f"Arista3 IP/Mac is: {ip_addr}/{mac_addr}")
        found2 = True

    if found1 and found2:
        print("Exiting...")
        break
print()
