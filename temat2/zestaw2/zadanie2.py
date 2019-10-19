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
    # JAK ZAKODOWAĆ TEKST?
    data['output'] = result
    return result

def decode(data):
    result = ""
    # JAK ROZKODOWAĆ TEKST?
    data['output'] = result
    return result

def initialize(data):
    data['output'] = ""
    data['input'] = read_file("input2.txt")

def main():
    data = {}
    initialize(data)
    
    data['key'] = find_value_input("Podaj klucz szyfrujący", "string")
    data['key'] = data['key'].replace(" ", "")

    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer",
        allowed_values=[1, 2])
    if command == 1:
        encode(data)
    elif command == 2:
        decode(data)

    return data['output']