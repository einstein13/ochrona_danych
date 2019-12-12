# -*- coding: UTF-8 -*-

from random import randint

from .maths import *
from commons import *

def initialize(data):
    data['options'] = {'randMax': 10**9, 'testsNumber': 30}
    return

def generate_e(data):
    m = (data['p'] - 1) * (data['q'] - 1)
    data['m'] = m
    divisor = 2
    while divisor > 1:
        e = randint(2, m)
        divisor = greatest_common_divisor(e, m)
    data['e'] = e
    return e

def generate_d(data):
    d = extended_common_divisor(data['e'], data['m'])
    data['d'] = d
    return d

def generate_keys(data):
    print("public key (d, n):")
    string = "%d\n%d" % (data['d'], data['n'])
    print(string)
    write_file(string, "public.key")
    print("private key (e, n):")
    string = "%d\n%d" % (data['e'], data['n'])
    print(string)
    write_file(string, "private.key")

def main():
    data = {}
    initialize(data)
    data['p'] = generate_prime(data)
    print("Liczba p: %d" % data['p'])
    data['q'] = generate_prime(data)
    print("Liczba q: %d" % data['q'])
    data['n'] = data['p'] * data['q']
    print("Liczba n: %d" % data['n'])
    generate_e(data)
    print("Liczba e: %d" % data['e'])
    generate_d(data)
    print("Liczba d: %d" % data['d'])
    print("generuję parę kluczy...")
    generate_keys(data)
    return ""