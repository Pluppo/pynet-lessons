#!/usr/bin/python3.6

from __future__ import division, print_function, unicode_literals
import readline

f = open("show_version.txt")

output = f.read()

print(output)
print(f"The file type is {type(output)}")

f.close()

with open("show_version.txt") as f:
    output = f.readlines()
    print(output)
    print(f"The file type is {type(output)}")
