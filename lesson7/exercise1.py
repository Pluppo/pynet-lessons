#!/usr/bin/env python3.6
import jinja2

vlan_template = '''
vlan {{ vlan_id }}
   name {{ vlan_name }}
'''

template_vars = {
    'vlan_id': 400,
    'vlan_name': 'red400'
}

template = jinja2.Template(vlan_template)
print(template.render(template_vars))

crypto_template = '''
{%- if isakmp_enable %}
crypto isakmp policy 10
 encr {{ encr }}
 authentication {{ auth }}
 group {{ dh_group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{%- endif%}
'''

crypto_vars = {
    'encr': 'aes',
    'auth': 'pre-share',
    'dh_group': 5,
    'isakmp_enable': True
}

t2 = jinja2.Template(crypto_template)
print(t2.render(crypto_vars))

vlan_dict = {str(vlan): 'blue'+str(vlan) for vlan in range(501,509)}

vlan_vars = {'vlans': vlan_dict}

vlan_dict_template = '''
{%- for vlan_id, vlan_name in vlans.items() %}
vlan {{ vlan_id }}
   name {{ vlan_name }}
{%- endfor %}
'''

t3 = jinja2.Template(vlan_dict_template)
print(t3.render(vlan_vars))
