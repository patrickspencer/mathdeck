from sympy import symbols
import json
import unicodedata
from pprint import pprint

with open('fixtures/fixture_1.json') as f:
    data = json.load(f)

vars = data['symbols'].replace(" ","").split(",")
pprint(vars)
# for (i, var) in vars:
#     var = symbols('')
# print variables
# key = eval(data['key'])
# pprint(key)
# print(type(key))
# pprint(eval(expr = data['key']))
