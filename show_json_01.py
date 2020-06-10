# -*- coding: utf-8 -*-

import json


def breakdown(data, level=0):
    position1 = ' ' * 3 * level
    if type(data) != list and type(data) != dict:
        print('\n', position1 + str(data) + ',', end='')
    elif type(data) == list:
        print('\n', position1, 'level ', level + 1, type(data))
        print(position1 + '[', end='')
        for x in data:
            breakdown(x, level + 1)
        print('\n', position1 + ']')
    elif type(data) == dict:
        print('\n', position1, 'level ', level + 1, type(data))
        print(position1 + '{')
        for x in data.items():
            print(position1 + x[0] + ': ', end="")
            if type(x[1]) != list and type(x[1]) != dict:
                print(str(x[1]) + ',')
            else:
                breakdown(x[1], level + 1)
        print(position1 + '}', end='')

filename = 'json_data_01.json'
with open(filename, encoding='UTF-8-sig') as file:
    data = json.load(file)

breakdown(data)
