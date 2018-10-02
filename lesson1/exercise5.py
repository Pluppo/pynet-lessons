#!/usr/bin/python3.6

from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.split()
mac2 = mac2.split()
mac3 = mac3.split()

columns = '{:>20} {:>20}'

print(columns.format("IP ADDR","MAC ADDRESS"))
print(columns.format("-" * 20,"-" * 20))
print(columns.format(mac1[1],mac1[3]))
print(columns.format(mac2[1],mac2[3]))
print(columns.format(mac3[1],mac3[3]))
