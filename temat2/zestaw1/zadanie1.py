# -*- coding: UTF-8 -*-

from commons import *

# za:
# https://pl.wikipedia.org/wiki/Alfabet_polski#Cz%C4%99sto%C5%9B%C4%87_wyst%C4%99powania_liter

letters_frequency = [
    ['a', 8.91+0.99],
    ['b', 1.47],
    ['c', 3.96+0.40],
    ['d', 3.25],
    ['e', 7.66+1.11],
    ['f', 0.30],
    ['g', 1.42],
    ['h', 1.08],
    ['i', 8.21],
    ['j', 2.28],
    ['k', 3.51],
    ['l', 2.10+1.82],
    ['m', 2.80],
    ['n', 5.52+0.20],
    ['o', 7.75+0.85],
    ['p', 3.13],
    ['q', 0.14],
    ['r', 4.69],
    ['s', 4.32+0.66],
    ['t', 3.98],
    ['u', 2.50],
    ['v', 0.04],
    ['w', 4.65],
    ['x', 0.02],
    ['y', 3.76],
    ['z', 5.64+0.06+0.83],
    ]
all_letters = [item[0] for item in letters_frequency]
for el in letters_frequency:
    el[1] /= 100
# letters_frequency.sort(key=lambda x: -x[1])

def substitute_letters(text, dictionary):
    # code / decode function
    text = str(text)
    result = ""
    for char in text:
        if char in dictionary:
            result += dictionary[char]
        else:
            result += char
    return result

def text_frequency(text):
    result = {}
    # initialize all letters
    for char in all_letters:
        result[char] = 0
    # count letters
    for char in text:
        if char in result:
            result[char] += 1
    total = 0
    # sum occurences
    for char in all_letters:
        total += result[char]
    # make occurances to frequences
    for char in all_letters:
        result[char] /= total
    # return result
    return result

def initialize(data):
    data['input'] = read_file("kryptogram.txt")
    data['dictionary'] = {}
    return

def decode(data):
    data['output'] = substitute_letters(data['input'], data['dictionary'])
    return

def show_help():
    print(" ")
    print("Witaj w programie wspomagającym rozkodowywanie tekstu.")
    print("Zakodowany tekst jest w pliku kryptogram.txt")
    print("Dostępne funkcje:")
    print("  0 - wyjście z programu, zakończenie pracy")
    print("  1 - wydrukowanie tekstu pomocy")
    print("  2 - wydrukowanie tekstu zakodowanego")
    print("  3 - wydrukowanie tekstu rozkodowanego (według ustalonego słownika)")
    print("  4 - porównanie tekstu rozkodowanego i zakodowanego")
    print("  5 - wyświetlenie słownika")
    print("  6 - pokazanie częstości w tekście zakodowanym")
    print("  7 - pokazanie częstości w języku polskim")
    print("  8 - porównanie częstości w tekście oraz w języku polskim")
    print("  9 - autodopasowanie słownika (na podstawie częstości znaków)")
    print("  10 - ustalenie pojedynczego znaku w słowniku")
    print(" ")
    return

def dict_to_table(dictionary):
    result = []
    for key in dictionary.keys():
        result.append([key, dictionary[key]])
    result.sort()
    return result

def show_dictionary(dicionary, headers=None):
    table = dict_to_table(dicionary)
    if headers:
        table = [headers] + table
    print_table(table)
    return

def main():
    data = {}
    initialize(data)

    print("0 - wyjście, 1 - pomoc")

    while True:
        command = find_value_input("\nPodaj numer funkcji", "integer")
        if command == 0:
            break
        elif command == 1:
            show_help()
        elif command == 2:
            value = find_value_input("Podaj ilość linii", "integer")
            print_long_text(data['input'], value)
        elif command == 3:
            decode(data)
            value = find_value_input("Podaj ilość linii", "integer")
            print_long_text(data['output'], value)
        elif command == 4:
            decode(data)
            value = find_value_input("Podaj ilość linii", "integer")
            compare_long_texts(data['input'], data['output'], value)
        elif command == 5:
            show_dictionary(data['dictionary'], ["klucz", "wartość"])
        elif command == 6:
            frequency = text_frequency(data['input'])
            show_dictionary(frequency, ["litera", "częstość"])
        elif command == 7:
            frequency = [["litera", "częstość"]] + letters_frequency
            print_table(frequency)
        else:
            print("* * * Funkcja nie istnieje * * *")
    return

main()