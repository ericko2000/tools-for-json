# -*- coding: utf-8 -*-

import json


def breakdown(json_data, level=0):  # A function to unfold json data # json_data - an object of json.load
    position1 = ' ' * 3 * level
    if type(json_data) != list and type(json_data) != dict:
        print('\n', position1 + str(json_data) + ',', end='')
    elif type(json_data) == list:
        print('\n', position1, 'level ', level + 1, type(json_data))
        print(position1 + '[', end='')
        for x in json_data:
            breakdown(x, level + 1)
        print('\n', position1 + ']')
    elif type(json_data) == dict:
        print('\n', position1, 'level ', level + 1, type(json_data))
        print(position1 + '{')
        for x in json_data.items():
            print(position1 + x[0] + ': ', end="")
            if type(x[1]) != list and type(x[1]) != dict:
                print(str(x[1]) + ',')
            else:
                breakdown(x[1], level + 1)
        print(position1 + '}', end='')


filename = 'json_data_01.json'
with open(filename, encoding='UTF-8-sig') as file:  # open a json file
    data = json.load(file)

breakdown(data)  # call function breakdown()
