#!/usr/bin/env python3.6
import yaml
from pprint import pprint

yaml_file3a = 'excercise3a.yml'
with open(yaml_file3a) as f:
    yaml_file3a = f.read()

int_list = yaml.load(yaml_file3a)
print()
print(int_list)

yaml_file3b = 'excercise3b.yml'
with open(yaml_file3b) as f:
    yaml_file3b = f.read()

int_vars = yaml.load(yaml_file3b)

print()
print('-' * 120)
pprint(int_vars)
