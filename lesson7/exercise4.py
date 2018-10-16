#!/usr/bin/env python3.6
import jinja2
import yaml

yaml_file3b = 'excercise3b.yml'
with open(yaml_file3b) as f:
    yaml_file3b = f.read()

int_vars = yaml.load(yaml_file3b)

jinja_template = 'exercise4.j2'
with open(jinja_template) as f:
    jinja_template = f.read()

template = jinja2.Template(jinja_template)
print(template.render(int_vars))
