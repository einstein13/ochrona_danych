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

    # TUTAJ DODAJ SPRAWDZANIE POPRAWNOŚCI ze względu na cyfrę kontrolną!

    return True

def pesel_sex(data):
    value = data['input_string'][9]
    value = int(value)
    if value % 2 == 0:
        return "kobieta"
    return "mężczyzna"

def main():
    data = {}
    initialize(data)

    print("Podanie numeru \"0\" oznacza zakończenie programu.\n")
    number = ""
    while number != "0":
        number = find_value_input("Podaj numer PESEL", "string")
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