# -*- coding: UTF-8 -*-

from .maths import *
from commons import *

def encrypt(data):
    values = []

    if data['debug']:
        print(data['original'])

    for char in data['original']:
        values.append(ord(char))
    if len(values) % 2 == 1:
        values.append(0)

    if data['debug']:
        print(values)

    glued = []
    for itr in range(len(values) // 2):
        new_value = "%03d%03d" % (values[2*itr], values[2*itr+1])
        new_value = int(new_value)
        glued.append(new_value)

    if data['debug']:
        print(glued)

    result = []
    for value in glued:
        new_value = power_modulo(value, data['e'], data['n'])
        result.append(new_value)

    if data['debug']:
        print(result)

    data['encrypted'] = ",".join(map(str,result))

    if data['debug']:
        print(data['encrypted'])

    return data['encrypted']

def decrypt(data):
    values = []

    if data['debug']:
        print(data['encrypted'])

    splitted = data['encrypted'].split(",")

    if data['debug']:
        print(splitted)

    glued = []
    for value in splitted:
        new_value = power_modulo(int(value), data['d'], data['n'])
        glued.append(new_value)

    if data['debug']:
        print(glued)

    values = []
    for new_value in glued:
        values.append(new_value // 1000)
        values.append(new_value % 1000)
    if values[-1] == 0:
        values.pop(-1)

    if data['debug']:
        print(values)

    result = []
    for char in values:
        result.append(chr(char))

    if data['debug']:
        print(result)

    data['decrypted'] = "".join(result)

    if data['debug']:
        print(data['decrypted'])

    return data['decrypted']

def initialize(data):
    data['original'] = ""
    data['encrypted'] = ""
    data['decrypted'] = ""
    data['public_key'] = read_file("public.key")
    data['private_key'] = read_file("private.key")
    d, n2 = data['public_key'].split("\n")
    e, n1 = data['private_key'].split("\n")
    if n1 != n2:
        print("Klucz prywatny i publiczny są niespójne!")
        return False
    d = int(d)
    e = int(e)
    n = int(n1)
    data['d'] = d
    data['e'] = e
    data['n'] = n

    data['debug'] = False
    return True

def main():
    data = {}
    ok = initialize(data)
    if not ok:
        return ""
    command = find_value_input("Zakoduj [1] czy rozkoduj [2]?", "integer", allowed_values=[1, 2])
    if command == 1:
        data['original'] = read_file("text.txt")
        result = encrypt(data)
        print("\nZaszyfrowana wiadomość:\n")
        print(result)
        write_file(result, "text.enc")
    elif command == 2:
        data['encrypted'] = read_file("text.enc")
        result = decrypt(data)
        print("\nRozszyfrowana wiadomość:\n")
        print(result)
        write_file(result, "text.dec")

    return ""