# -*- coding: UTF-8 -*-

from importlib import import_module
from os import chdir

from commons import find_value_input
from tasks import allowed_tasks

keys = list(allowed_tasks.keys())
value1 = find_value_input("Podaj numer tematu", 'integer', keys, 1)

keys = list(allowed_tasks[value1].keys())
value2 = find_value_input("Podaj numer zestawu", 'integer', keys, 2)

keys = allowed_tasks[value1][value2]
value3 = find_value_input("Podaj numer zadania", 'integer', keys, 3)

values = (value1, value2, value3)
print("Temat: %d, Zestaw: %d, Zadanie %d:" % values)

try:
    chdir("./temat%d/zestaw%d/" % (value1, value2))
    import_module("temat%d.zestaw%d.zadanie%d" % values)
except Exception as e:
    print("Coś poszło nie tak...")
    print(e)