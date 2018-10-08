#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline
import re

with open('show_ipv6_intf.txt') as f:
    sh_ipv6_int = f.read()

ipv6_addr1 = re.search(r'IPv6 address:\s+(\S+)', sh_ipv6_int, re.DOTALL).group(1)
ipv6_addr2 = re.search(r'\[VALID\]\s+(\S+)', sh_ipv6_int, re.DOTALL).group(1)

ipv6_list = [ipv6_addr1, ipv6_addr2]

print()
print(ipv6_list)
print()
