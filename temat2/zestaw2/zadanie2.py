# -*- coding: utf-8 -*-

from commons import *

def generateKey(data): 
    key = list(data['key']) 
    
    if len(data['plain_text']) == len(key): 
        return(key) 
    else: 
        for i in range(len(data['plain_text']) - 
            len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
    
def encode(data):
    key = data['generateKey']
    plaintext = data['plain_text']
    ciphertext = []
    
    for i in range(len(plaintext)): 
        x = (ord(plaintext[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext)) 

def decode(data):
    result = ""
    # JAK ROZKODOWAĆ TEKST?
    
    data['output'] = result
    return result

def initialize(data):
    data['output'] = ""
    data['plain_text'] = read_file("input1.txt")

def main():
    data = {}
    initialize(data)
    
    data['key'] = find_value_input("Podaj klucz szyfrujący", "string")
    data['key'] = data['key'].replace(" ", "")

    command = find_value_input("Zakoduj: 1 / Rozkoduj: 2", "integer",
        allowed_values=[1, 2])
    if command == 1:
        data['generateKey'] = generateKey(data)
        print('Tekst jawny:         ' + data['plain_text'])
        print('Tekst zaszyfrowany:  ' + encode(data))
    elif command == 2:
        decode(data)

    return data['output']