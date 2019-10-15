# -*- coding: UTF-8 -*-

from 

# za:
# https://pl.wikipedia.org/wiki/Alfabet_polski#Cz%C4%99sto%C5%9B%C4%87_wyst%C4%99powania_liter

letters_frequency = [
    ['a', 8.91+0.99],
    ['b', 1.47],
    ['c', 3.96+0.40],
    ['d', 3.25],
    ['e', 7.66+1.11],
    ['f', 0.30],
    ['g', 1.42],
    ['h', 1.08],
    ['i', 8.21],
    ['j', 2.28],
    ['k', 3.51],
    ['l', 2.10+1.82],
    ['m', 2.80],
    ['n', 5.52+0.20],
    ['o', 7.75+0.85],
    ['p', 3.13],
    ['q', 0.14],
    ['r', 4.69],
    ['s', 4.32+0.66],
    ['t', 3.98],
    ['u', 2.50],
    ['v', 0.04],
    ['w', 4.65],
    ['x', 0.02],
    ['y', 3.76],
    ['z', 5.64+0.06+0.83],
    ]
all_letters = [item[0] for item in letters_frequency]
for el in letters_frequency:
    el[1] /= 100
letters_frequency.sort(key=lambda x: -x[1])

def substitute_letters(text, dictionary):
    # code / decode function
    text = str(text)
    result = ""
    for char in text:
        if char in dictionary:
            result += dictionary[char]
        else:
            result += char
    return result

def get_sign(prompt='', typ='lowercase'):
    while True:
        result = input(prompt)
        if typ == 'lowercase':
            if len(result) != 1:
                continue
            if not result.islower():
                continue
            if result.isdigit():
                continue
            return result
        if typ == 'digit':
            if len(result) != 1:
                continue
            if not result.isdigit():
                continue
            return result
    return ""

