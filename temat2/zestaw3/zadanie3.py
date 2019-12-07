# -*- coding: UTF-8 -*-

from .maths import *
from commons import *

def encrypt(data):
    return ""

def decrypt(data):
    return ""

def initialize(data):
    data['encrypted'] = ""
    data['decrypted'] = ""
    data['public_key'] = read_file("public.key")
    data['private_key'] = read_file("private.key")
    d, n2 = data['public_key'].split("\n")
    e, n1 = data['private_key'].split("\n")
    if n1 != n2:
        print("Klucz prywatny i publiczny są niespójne!")
        return False


def main():
    data = {}
    ok = initialize(data)
    if not ok:
        return ""
    command = find_value_input("Zakoduj [1] czy rozkoduj [2]?", "integer", allowed_values=[1, 2])
    if command == 1:
        data['decrypted'] = ""

    return ""