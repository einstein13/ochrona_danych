# -*- coding: UTF-8 -*-

from commons import *

letters = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż', 'a', 'ą', 'b', 'c', 'ć', 'd', 'e',
        'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
        'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def encode(data):
    result = ""
    for char in data['input']:
        if char in letters:
            position = letters.index(char)
            position += data['shift']
            position = position % len(letters)
            result += letters[position]
        else:
            result += char
    data['output'] = result
    return result

def decode(data):
    data['shift'] = (-data['shift']) % len(letters)
    return decode(data)

def initialize(data):
    data['output'] = ""
    data['input'] = read_file("input2.txt")

def main():
    data = {}
    initialize(data)
    data['shift'] = find_value_input("Szyfr Cezara - Podaj wartość klucza (przesunięcia)",
        "integer", allowed_values=list(range(len(letters))))
    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer",
        allowed_values=[1, 2])
    if command == 1:
        print("Zaszyfrowany teskst to:  ")
        encode(data)
    elif command == 2:
        print("Rozszyfrowany teskst to:  ")
        decode(data)

    return data['output']