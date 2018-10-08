#!/usr/bin/env python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

import random

def ip_gen(base_subnet='10.10.10.'):
    fourth_octet = str(random.randint(1, 254))
    print(base_subnet + fourth_octet)

ip_gen()
ip_gen('172.16.0.')
ip_gen(base_subnet='192.168.0.')
