#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline

import re
import pdb

pdb.set_trace()

def mac_format(mac_addr):
    #Convert to upper case
    mac_addr = mac_addr.upper()
   
    #Split into octets and reassemble into list for : and - notations
    if ':' in mac_addr or '-' in mac_addr:
        new_mac = []
        octets = re.split(r'[-:]', mac_addr)
        #Check octet size, add padding if necessary
        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    #Split into octets and reassemble into list for . notations
    elif '.' in mac_addr:
        new_mac = []
        sections = mac_addr.split('.')
        #Check section size, add padding if necessary
        for word in sections:
            if len(word) < 4:
                word = word.zfill(4)
            new_mac.append(word[:2])
            new_mac.append(word[2:])
    new_mac = ':'.join(new_mac)

    print()
    print(new_mac)
    print()

mac_format('01:23:45:67:89:AB')
mac_format('0000.aaaa.bbbb')
mac_format('00-00-aa-aa-bb-bb')
mac_format('a:b:c:d:e:f')
