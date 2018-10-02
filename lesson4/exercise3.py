#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
from pprint import pprint
import readline
import re

with open('show_version.txt') as f:
    sh_ver = f.read()

version = re.search(r'Version (\S+),', sh_ver).group(1)
serial = re.search(r'^Processor board ID (\S+)', sh_ver, re.M).group(1)
conf_reg = re.search(r'^Configuration register is (\S+)', sh_ver, re.M).group(1)

print()
print("OS Version: {}".format(version))
print("Serial Number: {}".format(serial))
print("Config Register: {}".format(conf_reg))
print()
