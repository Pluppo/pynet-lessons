#!/usr/bin/env python3.6

from __future__ import print_function, unicode_literals
import readline

ip_addr = input("Please enter an IP address:")

octets = ip_addr.split('.')

style_format = "{:^15}{:^15}{:^15}{:^15}"

print(style_format.format("Octet1","Octet2","Octet3","Octet4"))
print("-" * 60)
print(style_format.format(*octets))
print(style_format.format(bin(int(octets[0])),bin(int(octets[1])),bin(int(octets[2])),bin(int(octets[3]))))
print(style_format.format(hex(int(octets[0])),hex(int(octets[1])),hex(int(octets[2])),hex(int(octets[3]))))
print("-" * 60)
