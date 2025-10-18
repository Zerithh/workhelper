# import datetime as d, sys, os, platform

# from math import sqrt as s, ceil
# # print(d.datetime.now().time().hour)

# print(ceil(s(25)))

import json

name1 = input('Введіть своє імя: ')
age2 = input('Введіть свій вік: ')

data = {'name': name1, 'age': age2}

with open('name.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('name.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

print(loaded['name'], loaded['age'])