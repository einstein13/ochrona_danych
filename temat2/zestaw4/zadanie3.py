# -*- coding: UTF-8 -*-

from commons import *

base = 2**8
debug = False

def initialize(data):
    data['output'] = ""
    data['input'] = ""

def find_base_power(target_value):
    result = base
    while result < target_value:
        result *= base
    return result

def transform_text_to_value(data):
    result = 0
    for char in data['input_text']:
        value = ord(char)
        result *= find_base_power(value)
        result += value
    data['input_value'] = result
    return result

def log2(value):
    itr = 0
    val = value
    while val > 0:
        val //= 2
        itr += 1
    return itr

def prepare_to_crc(data):
    # preparing text value
    preparing = data['input_value']
    preparing *= base
    preparing //= 2
    data['crc_input'] = preparing
    log2input = log2(preparing)

    # preparing crc divisor
    log2divisor = log2(data['divisor'])
    data['crc_steps'] = log2input - log2(base) + 2
    data['crc_divisor'] = data['divisor'] * (2**(log2input - log2divisor))
    return True


def crc(data):
    prepare_to_crc(data)
    itr = data['crc_steps']
    divisor = data['crc_divisor']
    value = data['crc_input']

    pattern = "%d"
    while itr > 0:
        if debug:
            print(" ")
            pattern = "%%0%dd" % log2(divisor)
            print(pattern)
            v = int(str(bin(value))[2:])
            print(pattern % v)
            v = int(str(bin(divisor))[2:])
            print(pattern % v)

        if log2(value) == log2(divisor):
            value = value ^ divisor
            if debug:
                print(pattern % int(str(bin(value))[2:]))
        itr -= 1
        divisor //= 2
    return value

def main():
    data = {}
    initialize(data)
    print("Podanie wartości dzielnika jako %d oznacza zakończenie programu." % base)

    divisor = base
    while divisor != 0:
        print(" ")
        divisor = find_value_input("Wartość dzielnika (wielomianu)", "integer", allowed_values=[0, base])
        if divisor == base:
            break
        data['divisor'] = divisor

        data['input_text'] = find_value_input("Podaj ciąg znaków", "string")
        transform_text_to_value(data)
        result = crc(data)
        print("Suma CRC wynosi %d" % result)
        print("Binarnie: %s" % str(bin(result))[2:])

    return ""