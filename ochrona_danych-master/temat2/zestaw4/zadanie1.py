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

    value10 = data['input_string'][10]
    value10 = int(value10)



    # print (value1)
    # print (value2)
    # print (value3)
    # print (value4)
    # print (value10)

    suma = (1*(value1)) + (3*(value2)) + (7*(value3)) + (9*(value4)) + (1*(value5)) + (3*(value6)) + (7*(value7)) + (9*(value8)) + (1*(value9)) + (3*(value10))
    suma = int(suma)
    print (suma)

    kontrolka=10-(suma %10)
    print (kontrolka)

    if kontrolka== 10:
        kontrolka= 0
    else:
        kontrolka=kontrolka
 
    #kontrolka i sprawdzenie zgodnosci
    if ((kontrolka== 10)or(kontrolka== 0)):
        return 0
    else:
        return 1
 
    

    # if (kontrolka==10) or (data==kontrolka): #w przypadku liczby kontrolnej 10 i 0 sa jednoznaczne a 0 moze byc wynikiem odejmowania
    #     return "DUPA" ##domyslana wartosc logczna dla ifa klasy roboczej
    # else:
    #     return "SUMA" ##domyslna wartosc logiczna dla elsa



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
            print("Suma kontrolna %s" % pesel_chksum(data))
        
        else:
            print("Numer PESEL jest niepoprawny")




    return ""