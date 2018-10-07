#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

with open("show_ip_bgp_summ.txt") as show_ip_bgp_summ:
    output = show_ip_bgp_summ.read()
    output = output.splitlines()
    firstline = output[0].split()
    lastline = output[-1].split()
    as_nr = firstline[-1]
    peer_ip = lastline[0]
    print(f"BGP peer AS number is: {as_nr}")
    print(f"BGP peer IP is: {peer_ip}")
