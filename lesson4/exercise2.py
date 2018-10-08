#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

houston_dc_rtr = ['10.217.70.98', '10.229.45.51', '10.123.91.222', '10.250.48.235', '10.234.54.178', '10.170.47.154', '10.29.43.240', '10.228.109.228', '10.21.142.132', '10.62.56.175', '10.108.14.6', '10.201.187.10', '10.228.109.228', '10.21.142.132', '10.62.56.175']

atlanta_dc_rtr = ['10.217.70.98', '10.229.45.51', '10.123.91.222', '10.55.231.181', '10.25.181.12', '10.253.217.224', '10.31.220.126', '10.130.39.47', '10.179.96.247', '10.243.242.84', '10.21.208.144', '10.187.250.49', '10.82.222.247', '10.110.135.161', '10.147.64.241']

chicago_dc_rtr = ['10.217.70.98', '10.234.54.178', '10.170.47.154', '10.130.39.47', '10.179.96.247', '10.243.242.84', '10.247.4.170', '10.20.206.181', '10.131.255.93', '10.67.20.139', '10.43.1.68', '10.167.226.11', '10.41.20.157', '10.165.183.11', '10.56.173.176']

houston_dc_rtr = set(houston_dc_rtr)
atlanta_dc_rtr = set(atlanta_dc_rtr)
chicago_dc_rtr = set(chicago_dc_rtr)

print("Common IP's in Houston and Atlanta:")
pprint(houston_dc_rtr & atlanta_dc_rtr)
print()
print("Common IP's in all sites:")
pprint(houston_dc_rtr & atlanta_dc_rtr & chicago_dc_rtr)
print()
print("Unique IP's in Chicago:")
pprint(chicago_dc_rtr - atlanta_dc_rtr - houston_dc_rtr)
