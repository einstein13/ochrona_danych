# -*- coding: UTF-8 -*-

from json import loads, dumps

from .maths import *
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

    return ""