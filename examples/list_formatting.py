#!/usr/bin/python3.6
from __future__ import print_function, unicode_literals

ip_addr = '192.168.1.1'
octets = ip_addr.split('.')

print("\n")
print("-" * 80)
print("{:10}{:10}{:10}{:10}".format(*octets)) # * sign makes format treat each list item as a separate object
print("-" * 80)
print("\n")
