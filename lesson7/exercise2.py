#!/usr/bin/env python3.6
import jinja2

template_vars = {
     'ospf_process_id': '10',
     'ospf_priority': '100',
     'ospf_active_interfaces': ['Vlan1', 'Vlan2'],
     'ospf_area0_networks': ['10.10.10.0/24', '10.10.20.0/24', '10.10.30.0/24']
}

template_vars2 = {
     'ospf_process_id': '1',
     'ospf_active_interfaces': ['Vlan10', 'Vlan22'],
     'ospf_area0_networks': ['10.10.11.0/24', '10.10.21.0/24', '10.10.31.0/24']
}

template_file = 'exercise2.j2'
with open(template_file) as f:
    jinja_template = f.read()

template = jinja2.Template(jinja_template)
print('-' * 80)
print(template.render(template_vars))
print('-' * 80)
print(template.render(template_vars2))
print('-' * 80)
