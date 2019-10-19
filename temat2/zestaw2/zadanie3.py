# -*- coding: UTF-8 -*-

from commons import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

def generate_matrix_key(data):
    # na podstawie data['key'] wygeneruj data['matrix_key']
    # podpowiedź: pomiń znaki nie będące w zmiennej letters (char not in letters)
    return

def initialize(data):
    data['output'] = ""
    data['input'] = read_file("input2.txt")
    return

def main():
    data = {}
    initialize(data)
    
    data['key'] = find_value_input("Podaj klucz szyfrujący", "string")
    generate_matrix_key(data)

    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer",
        allowed_values=[1, 2])
    if command == 1:
        encode(data)
    elif command == 2:
        decode(data)

    return data['output']