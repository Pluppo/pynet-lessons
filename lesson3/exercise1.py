#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

vlan_list = []
with open('show_vlan.txt') as show_vlan:
    show_vlan = show_vlan.read()

for line in show_vlan.splitlines():
    if 'VLAN' in line or '-----' in line or line.startswith('      '):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()
