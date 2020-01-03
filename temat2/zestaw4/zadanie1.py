# -*- coding: UTF-8 -*-
from commons import *

def initialize(data):
    data['output'] = ""
    data['input'] = ""

def validate_pesel(data):
    input_string = data['input_string']
    if len(input_string) != 11:
        return False
    if not input_string.isdigit():
        return False

    input_number = int(input_string)

    return pesel_chksum(data) == "OK"

def pesel_sex(data):
    value = data['input_string'][9]
    value = int(value)
    if value % 2 == 0:
        return "kobieta"
    return "mężczyzna"

def pesel_chksum(data):
    value1 = data['input_string'][0]
    value1 = int(value1)
    value2 = data['input_string'][1]
    value2 = int(value2)
    value3 = data['input_string'][2]
    value3 = int(value3)
    value4 = data['input_string'][3]
    value4 = int(value4)
    value5 = data['input_string'][4]
    value5 = int(value5)
    value6 = data['input_string'][5]
    value6 = int(value6)
    value7 = data['input_string'][6]
    value7 = int(value7)
    value8 = data['input_string'][7]
    value8 = int(value8)
    value9 = data['input_string'][8]
    value9 = int(value9)

    value10 = data['input_string'][9]
    value10 = int(value10)

    value11 = data['input_string'][10]
    value11 = int(value11)


    suma = (9*(value1)) + (7*(value2)) + (3*(value3)) + (1*(value4)) + (9*(value5)) + (7*(value6)) + (3*(value7)) + (1*(value8)) + (9*(value9)) + (7*(value10))
    suma = int(suma)

    mod = suma % 10

    if mod == value11:
        return "OK"
    return "FAIL"

def main():
    data = {}
    initialize(data)

    print("Podanie numeru \"0\" oznacza zakończenie programu.")
    number = ""
    while number != "0":
        number = find_value_input("\nPodaj numer PESEL", "string")
        if number == "0":
            break
        data['input_string'] = number

        validated = validate_pesel(data)

        if validated:
            print("Podany numer PESEL jest poprawny")
            print("Osoba z podanym numerem PESEL to %s" % pesel_sex(data))
        
        else:
            print("Numer PESEL jest niepoprawny")

    return ""