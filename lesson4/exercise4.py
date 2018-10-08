#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

match = re.search(r'^Cisco (?P<model>\S+).*with (?P<memory>\S+)', show_version, re.M)
model = match.groupdict()['model']
memory = match.groupdict()['memory']

print()
print("Model: {}".format(model))
print("Memory: {}".format(memory))
print()
