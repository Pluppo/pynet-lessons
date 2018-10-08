#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

with open("show_arp.txt") as show_arp:
    output = show_arp.readlines()
    output = output[1:]
    pprint(output)
    output.sort()
    arp_output = output[:3]
    arp_output = '\n'.join(arp_output)
    with open("arp_entries.txt", "w") as arp_entries:
        arp_entries.write(arp_output)
