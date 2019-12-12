# -*- coding: utf-8 -*-

from commons import *

letters = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż', 'a', 'ą', 'b', 'c', 'ć', 'd', 'e',
        'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
        'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generateKey(data): 
    key = list(data['key']) 
    
    if len(data['plain_text']) == len(key): 
        return(key) 
    else: 
        for i in range(len(data['plain_text']) - 
            len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key))

def position(character):
    global letters
    if character not in letters:
        return -1
    return letters.index(character)
    
def encode(data):
    global letters
    key = data['generateKey']
    plaintext = data['plain_text']
    ciphertext = []
    
    for i in range(len(plaintext)):
        x = position(plaintext[i])
        if x < 0: # characters that are not in our letters base
            ciphertext.append(plaintext[i])
            continue
        x += position(key[i])
        x = x % len(letters)
        ciphertext.append(letters[x])
    data['output'] = "".join(ciphertext)
    return data['output']

def decode(data):
    global letters
    key = data['generateKey']
    plaintext = data['plain_text']
    ciphertext = []
    
    for i in range(len(plaintext)):
        x = position(plaintext[i])
        if x < 0: # characters that are not in our letters base
            ciphertext.append(plaintext[i])
            continue
        x -= position(key[i])
        x = x % len(letters)
        ciphertext.append(letters[x])
    data['output'] = "".join(ciphertext)
    return data['output']

def initialize(data):
    data['output'] = ""
    data['plain_text'] = read_file("input2.txt")

def main():
    data = {}
    initialize(data)
    
    data['key'] = find_value_input("Podaj klucz szyfrujący", "string")
    data['key'] = data['key'].replace(" ", "")

    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer",
        allowed_values=[1, 2])
    if command == 1:
        data['generateKey'] = generateKey(data)
        encode(data)
    elif command == 2:
        data['generateKey'] = generateKey(data)
        decode(data)

    return data['output']