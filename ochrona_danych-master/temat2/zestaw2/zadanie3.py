# -*- coding: UTF-8 -*-

from commons import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# sugestia: użyj funkcji find_in_matrix z pliku commons.py (jest już dostępna)
# pozwala ona znaleźć pozycję elementu w formie [X, Y] z 2-wymiarowej tabeli

def mapping(character):
    values = {
        'a': 'AaĄą',
        'b': 'Bb',
        'c': 'CcĆć',
        'd': 'Dd',
        'e': 'EeĘę',
        'f': 'Ff',
        'g': 'Gg',
        'h': 'Hh',
        'i': 'IiJj',
        'k': 'Kk',
        'l': 'LlŁł',
        'm': 'Mm',
        'n': 'NnŃń',
        'o': 'OoÓó',
        'p': 'Pp',
        'q': 'Qq',
        'r': 'Rr',
        's': 'SsŚś',
        't': 'Tt',
        'u': 'Uu',
        'v': 'Vv',
        'w': 'Ww',
        'x': 'Xx',
        'y': 'Yy',
        'z': 'ZzŹźŻż'
    }
    for key in values.keys():
        if character in values[key]:
            return key
    return None

def encode_pair(data, pair):
    result = ""
    position1 = find_in_matrix(pair[0], data['matrix_key'])
    position2 = find_in_matrix(pair[1], data['matrix_key'])

    if position1[0] == position2[0]:
        position1[1] = (position1[1] + 1) % 5
        position2[1] = (position2[1] + 1) % 5
    elif position1[1] == position2[1]:
        position1[0] = (position1[0] + 1) % 5
        position2[0] = (position2[0] + 1) % 5
    else:
        position1[1], position2[1] = position2[1], position1[1]

    result += data['matrix_key'][position1[0]][position1[1]]
    result += data['matrix_key'][position2[0]][position2[1]]
    return result

def encode(data):
    pair = []
    result = ""
    between = ""
    for letter in data['input']:
        mapped = mapping(letter)
        if mapped is None:
            if len(pair) == 0:
                result += letter
            else:
                between += letter
            continue
        pair.append(mapped)

        if len(pair) == 2:
            text = encode_pair(data, pair)
            result += text[0] + between + text[1]
            between = ""
            pair = []

    if len(pair) == 1:
        pair.append("z")
        result += encode_pair(data, pair)

    data['output'] = result
    return result

def decode_pair(data, pair):
    result = ""
    position1 = find_in_matrix(pair[0], data['matrix_key'])
    position2 = find_in_matrix(pair[1], data['matrix_key'])

    if position1[0] == position2[0]:
        position1[1] = (position1[1] - 1) % 5
        position2[1] = (position2[1] - 1) % 5
    elif position1[1] == position2[1]:
        position1[0] = (position1[0] - 1) % 5
        position2[0] = (position2[0] - 1) % 5
    else:
        position1[1], position2[1] = position2[1], position1[1]

    result += data['matrix_key'][position1[0]][position1[1]]
    result += data['matrix_key'][position2[0]][position2[1]]
    return result

def decode(data):
    pair = []
    result = ""
    between = ""
    for letter in data['input']:
        mapped = mapping(letter)
        if mapped is None:
            if len(pair) == 0:
                result += letter
            else:
                between += letter
            continue
        pair.append(letter)

        if len(pair) == 2:
            text = decode_pair(data, pair)
            result += text[0] + between + text[1]
            between = ""
            pair = []

    if len(pair) == 1:
        pair.append("z")
        result += encode_pair(data, pair)

    print(result)
    data['output'] = result
    return result

def generate_matrix_key(data):
    global letters
    unused = list(letters)

    new_key = []
    for char in data['key']:
        mapped = mapping(char)
        if mapped is None:
            continue
        if mapped in unused:
            index = unused.index(mapped)
            new_key.append(unused.pop(index))
    new_key += unused

    matrix_key = []
    for itr in range(5):
        matrix_key.append(new_key[itr*5:(itr+1)*5])
    data['matrix_key'] = matrix_key
    return matrix_key

def initialize(data):
    data['output'] = ""
    data['input'] = read_file("input3.txt")
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