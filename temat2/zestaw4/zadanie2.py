# -*- coding: UTF-8 -*-

from commons import *

def initialize(data):
    data['output'] = ""
    data['input'] = ""

def is_plain_number(data):
    if data['input'].isdigit():
        return True
    return False

def is_validated_number(data):
    if not data['input'][:-2].isdigit():
        return False
    if not data['input'][-2] == "-":
        return False
    if not data['input'][-1].isdigit():
        return False
    return True

def luhn_validation(number_string):
    result = 0

    for itr in range(len(number_string)):
        multiplier = 1
        if itr % 2 == 0:
            multiplier += 1
        value = int(number_string[-itr-1])
        value *= multiplier
        if value >= 10:
            value = value // 10 + value % 10
        result += value

    result = result % 10
    if result != 0:
        result = 10 - result

    return result

def add_validation(data):
    data['output'] = data['input']
    data['output'] += "-" + str(luhn_validation(data['input']))
    return data['output']

def check_validation(data):
    check_value = luhn_validation(data['input'][:-2])
    return str(check_value) == data['input'][-1]

def main():
    data = {}
    initialize(data)

    number = ""
    print("Podanie numeru \"0\" oznacza zakończenie programu.\n")
    while number != "0":
        number = find_value_input("Podaj wartość", "string")
        if number == "0":
            break
        data['input'] = number

        if is_plain_number(data):
            add_validation(data)
            print("Ciąg z cyfrą kontrolną wynosi: %s" % data['output'])
        elif is_validated_number(data):
            result = check_validation(data)
            if result:
                print("Wartość %s jest poprawną cyfrą kontrolną" % data['input'][-1])
            else:
                print("%s jest błędną cyfrą kontrolną" % data['input'][-1])
        else:
            print("Niepoprawny ciąg [%s]" % data['input'])

    return ""