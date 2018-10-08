#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

with open("show_ip_int_brief.txt") as show_ip_int_brief:
    siib_list = show_ip_int_brief.readlines()
    siib_fa4_list = siib_list[5].split()
    siib_fa4_tuple = tuple(siib_fa4_list[:2])
    print(siib_fa4_tuple)
