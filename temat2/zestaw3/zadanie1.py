# -*- coding: UTF-8 -*-

from json import loads, dumps
from random import randint

from commons import *

def initialize(data):
    data['options'] = loads(read_file("options1.json"))
    if 'randMax' not in data['options']:
        data['options']['randMax'] = 10**9
    if 'testsNumber' not in data['options']:
        data['options']['testsNumber'] = 30
    return

def setOptions(data):
    old = data['options']['randMax']
    new = find_value_input("Podaj nowy zakres losowania [0 oznacza %d]" % old, "integer")
    if new != 0:
        data['options']['randMax'] = new
    old = data['options']['testsNumber']
    new = find_value_input("Podaj nową ilość testów [0 oznacza %d]" % old, "integer") 
    if new != 0:
        data['options']['testsNumber'] = new
    write_file(dumps(data['options']), "options1.json")

def greatest_common_divisor(number1, number2):
    a = number1
    b = number2
    while a > 0:
        a, b = b%a, a
    return b

def power_modulo(base, power, modulo):
    maximum = 1
    current = base % modulo

    powers = {1: current}
    while maximum < power:
        maximum *= 2
        current = (current * current) % modulo
        powers[maximum] = current

    current = power
    result = 1
    while maximum > 0:
        if current >= maximum:
            result *= powers[maximum]
            result = result % modulo
            current -= maximum
        maximum //= 2

    return result

def fermat_test(number, data):
    for itr in range(data['options']['testsNumber']):
        to_test = randint(1, number-1)
        divisor = greatest_common_divisor(to_test, number)
        if divisor > 1:
            return False
        power_value = power_modulo(to_test, number-1, number)
        if power_value != 1:
            return False
    return True

def random_odd(data):
    result = 0
    while result % 2 == 0:
        result = randint(1, data['options']['randMax'])
    return result

def main():
    data = {}
    initialize(data)
    command = 0
    print("\n0 - opcje\n1 - losuj liczbę\n2 - podaj liczbę\n3 - wylosuj potencjalnie pierwszą\n4 - wyjście\n")
    while command < 4:
        command = find_value_input("Podaj funkcję", "integer", allowed_values=[0, 1, 2, 3, 4])

        if command == 0:
            setOptions(data)
        elif command == 1:
            value_to_test = random_odd(data)
            print("Wylosowana liczba: %d" % value_to_test)
        elif command == 2:
            value_to_test = get_input("Podaj liczbę do sprawdzenia", "integer", {'min': 2})
        if command == 1 or command == 2:
            result = fermat_test(value_to_test, data)
            if result:
                print("Liczba może być pierwsza\n")
            else:
                print("Liczba jest złożona\n")
        if command == 3:
            result = False
            while not result:
                value_to_test = random_odd(data)
                result = fermat_test(value_to_test, data)
            print("Liczba %d jest potencjalnie pierwsza\n" % value_to_test)

    return data['output']