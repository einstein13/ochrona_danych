# -*- coding: UTF-8 -*-

from importlib import import_module
from os import chdir

from commons import find_value_input, write_file
from tasks import allowed_tasks

keys = list(allowed_tasks.keys())
value1 = find_value_input("\n Podaj numer tematu: \n Tenat 2 - Szyfry Polialfabetyczne", 'integer', keys, 1)

keys = list(allowed_tasks[value1].keys())
value2 = find_value_input("\n Podaj numer zestawu: \n 1 - Kryptoanaliza i szyfr polialfabetyczny, \n 2 - Szyfr Cezara, Vigenère'a, Playfair", 'integer', keys, 2)

keys = allowed_tasks[value1][value2]
if value2 == 1:
    value3 = find_value_input("\n Podaj numer zadania: \n 1 - Kryptoanaliza tekstu \n 2 - Szyfrowania tekstem podstawieniowym polialfabetycznym", 'integer', keys, 3)
elif value2 == 2:
    value3 = find_value_input("\n Podaj numer zadania: \n 1 - Szyfr Cezara \n 2 - Szyfr Vigenère'a \n 3 - Szyfr Playfair", 'integer', keys, 3)

values = (value1, value2, value3)
print("Temat: %d, Zestaw: %d, Zadanie %d:" % values)

try:
    chdir("./temat%d/zestaw%d/" % (value1, value2))
    module = import_module("temat%d.zestaw%d.zadanie%d" % values)
    result = module.main()

    if result:
        write_file(result, "output%d.txt" % value3)
        print("\n" + result + "\n")

except Exception as e:
    print("Coś poszło nie tak...")
    print(e)