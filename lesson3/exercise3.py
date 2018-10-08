#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp_neighbors_detail = f.read()

style = "{:<15}  {:<15}"

sys_name, port_id = (None, None)

for line in show_lldp_neighbors_detail.splitlines():
    if 'System Name' in line:
        _, sys_name = line.split('System Name: ')
    elif 'Port id' in line:
        _, port_id = line.split('Port id: ')
    
    if sys_name and port_id:
        print(style.format("-" * 15, "-" * 15))
        print(style.format("System Name", sys_name))
        print(style.format("Port ID", port_id))
        print(style.format("-" * 15, "-" * 15))
        break
