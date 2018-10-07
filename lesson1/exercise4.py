#!/usr/bin/python3.6

from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()

show_version_list = show_version.split()

print("-" * 60)
print("Does the model string contain ""Cisco""?")
print("Cisco".lower() in show_version_list[1].lower())
print("-" * 60, "\n")
print("Does the model string contain ""881""?")
print("881" in show_version_list[1])
print("-" * 60, "\n")
print(f"Serial number: {show_version_list[2]}\nModel: {show_version_list[1]}")
print("-" * 60)
