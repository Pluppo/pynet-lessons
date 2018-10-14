#Example for printing all values of key 'my_key' in dictionary 'my_dict':
#for x in gen_dict_extract(my_dict, 'my_key'):
#    print(x)

def gen_dict_extract(var, key):
     if isinstance(var, dict):
         for k, v in var.items():
             if k == key:
                 yield v
             if isintance(v, (dict, list)):
                 yield from gen_dict_extract(v, key)
             elif isinstance(var, list):
                 for d in var:
                     yield from gen_dict_extract(d, kek)
