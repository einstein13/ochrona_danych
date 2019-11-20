# -*- coding: UTF-8 -*-

from sys import argv
from shutil import get_terminal_size

def get_input(prompt='', typ='lowercase', kwargs={}):
    while True:
        result = input(prompt+": ")
        if typ == 'lowercase':
            if len(result) != 1:
                continue
            if not result.islower():
                continue
            if result.isdigit():
                continue
            return result
        elif typ == 'digit':
            if len(result) != 1:
                continue
            if not result.isdigit():
                continue
            result = int(result)
            return result
        elif typ == 'integer':
            if not result.isdigit():
                continue
            result = int(result)
            if 'min' in kwargs and result < kwargs['min']:
                continue
            if 'max' in kwargs and result > kwargs['max']:
                continue
            return result
        elif typ == "string":
            return result
    return ""

def find_value_input(user_prompt, value_type, allowed_values=[], argument_position=None):
    if argument_position and len(argv) > argument_position:
        result = argv[argument_position]
        if value_type == 'integer':
            try:
                result = int(result)
            except Exception as e:
                pass
        if result in allowed_values:
            return result
    if allowed_values:
        if 'comment' in allowed_values:
            print("\n" + allowed_values['comment'])
            allowed_values.pop('comment')
        kwargs = {'min': min(list(allowed_values)), 'max': max(list(allowed_values))}
        result = get_input(user_prompt, typ=value_type,
            kwargs=kwargs)
    else:
        result = get_input(user_prompt, typ=value_type)
    return result

def read_file(name):
    file = open(name, "r")
    content = file.read()
    file.close()
    return content

def write_file(data, name):
    file = open(name, "w")
    file.write(str(data))
    file.close()
    return

def print_long_text(long_text, lines_number=None):
    signs_per_line = get_terminal_size().columns - 1
    lines_max = len(long_text) // signs_per_line
    if lines_max * signs_per_line < len(long_text):
        lines_max += 1
    if lines_number is not None and lines_max > lines_number and lines_number > 0:
        lines_max = lines_number

    itr = 0
    while itr < lines_max:
        print(long_text[itr*signs_per_line: (itr+1)*signs_per_line])
        itr += 1
    return

def compare_long_texts(text1, text2, lines_number=None):
    signs_per_line = get_terminal_size().columns - 1
    text_length = min(len(text1), len(text2))
    lines_max = text_length // signs_per_line
    if lines_max * signs_per_line < text_length:
        lines_max += 1
    if lines_number is not None and lines_max > lines_number and lines_number > 0:
        lines_max = lines_number

    itr = 0
    while itr < lines_max:
        print(text1[itr*signs_per_line: (itr+1)*signs_per_line])
        print(text2[itr*signs_per_line: (itr+1)*signs_per_line])
        print(" ")
        itr += 1
    return

def value_to_string(value, short=False):
    if type(value) in [str, int]:
        return str(value)
    if type(value) is float:
        return "%.4g" % value
    return str(value)

def merge_tables(table1, table2):
    if len(table1) != len(table2):
        return []
    result = []
    for itr in range(len(table1)):
        result.append(table1[itr] + table2[itr])
    return result

def transpose(table):
    result = []
    for itr1 in range(len(table[0])):
        result.append([])
        for itr2 in range(len(table)):
            result[itr1].append(table[itr2][itr1])
    return result

def find_in_matrix(element, table):
    for itr1 in range(len(table)):
        for itr2 in range(len(table[itr1])):
            if element == table[itr1][itr2]:
                return [itr1, itr2]
    return [-1, -1]

def print_table(table_data):
    if len(table_data) == 0:
        return
    table = []
    for itr1 in range(len(table_data)):
        table.append([])
        for itr2 in range(len(table_data[0])):
            table[itr1].append(value_to_string(table_data[itr1][itr2]))

    # length of columns
    lengths = [0] * len(table[0])
    for itr1 in range(len(table)):
        row = table[itr1]
        for itr2 in range(len(row)):
            if len(row[itr2]) > lengths[itr2]:
                lengths[itr2] = len(row[itr2])
    for itr1 in range(len(lengths)):
        lengths[itr1] += 2

    # print header
    line_to_print = "┌" + "─" * (lengths[0])
    for itr1 in range(1, len(lengths)):
        line_to_print += "┬" + "─" * (lengths[itr1])
    line_to_print += "┐"
    print(line_to_print)

    line_to_print = ""
    for itr1 in range(len(lengths)):
        element = table[0][itr1]
        additional_spaces = (lengths[itr1] - len(element) -1)
        line_to_print += "│ " + element + " " * additional_spaces
    line_to_print += "│"
    print(line_to_print)

    line_to_print = "├" + "─" * (lengths[0])
    for itr1 in range(1, len(lengths)):
        line_to_print += "┼" + "─" * (lengths[itr1])
    line_to_print += "┤"
    print(line_to_print)

    # print body
    for itr1 in range(1, len(table)):
        line_to_print = ""
        row = table[itr1]
        for itr2 in range(len(row)):
            element = row[itr2]
            additional_spaces = (lengths[itr2] - len(element) -1)
            line_to_print += "│ " + element + " " * additional_spaces
        line_to_print += "│"
        print(line_to_print)

    # end table
    line_to_print = "└" + "─" * (lengths[0])
    for itr1 in range(1, len(lengths)):
        line_to_print += "┴" + "─" * (lengths[itr1])
    line_to_print += "┘"
    print(line_to_print)

    return