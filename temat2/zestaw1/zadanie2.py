from commons import *
from json import dumps, loads
from random import choice, shuffle

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def generate_key(data):
    result = []
    used = []
    for char in chars:
        key = ""
        while key == "" or key in used:
            key = ""
            key += choice(chars)
            key += choice(chars)
        result.append([char, key])
    shuffle(result)
    return result

def read_or_generate_key(data):
    try:
        key = read_file("key2.txt")
        key = loads(key)
    except:
        key = generate_key(data)
        write_file(dumps(key), "key2.txt")
    data['key'] = key
    [data['chars'], data['keys']] = transpose(key)
    return

def initialize(data):
    data['output'] = ''
    data['input'] = read_file("input2.txt")
    read_or_generate_key(data)
    return

def encode_message(data):
    text = data['input']
    encoded = ""
    itr = 0
    itr_max = len(text)
    keys_max = len(data['chars'])
    while itr < itr_max:
        position = data['chars'].index(text[itr])
        if position > -1:
            position += itr
            position = position % keys_max
            encoded += data['keys'][position]
        else:
            encoded += text[itr]*2
        itr += 1
    data['output'] = encoded
    return encoded

def decode_message(data):
    text = data['input']
    decoded = ""
    itr = 0
    itr_max = len(text)//2
    keys_max = len(data['chars'])
    while itr < itr_max:
        to_decode = text[2*itr: 2*itr+2]
        position = data['keys'].index(to_decode)
        if position > -1:
            position -= itr
            position = position % keys_max
            decoded += data['chars'][position]
        else:
            if to_decode[0] == to_decode[1]:
                decoded += to_decode[0]
            else:
                print("Nie udało mi się przetłumaczyć [%s]" % to_decode)
        itr += 1
    data['output'] = decoded
    return decoded

def main():
    data = {}
    initialize(data)
    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer", allowed_values=[1, 2])
    if command == 1:
        encode_message(data)
    elif command == 2:
        decode_message(data)
    return data['output']