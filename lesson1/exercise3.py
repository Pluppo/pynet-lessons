#!/usr/bin/python3.6

from __future__ import print_function, unicode_literals

ip_addr = '2001:db8::1/64'
IP_ADDR = '2001:db8::2/64'
ipv6_addr = '2001:db8::3/64'

print(f"{ip_addr} is equal to {IP_ADDR}")
print(ip_addr == IP_ADDR)
print()
print(f"{ip_addr} is not equal to {ipv6_addr}")
print(ip_addr != ipv6_addr)
