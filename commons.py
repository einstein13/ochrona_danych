# -*- coding: UTF-8 -*-

from sys import argv

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
        if typ == 'digit':
            if len(result) != 1:
                continue
            if not result.isdigit():
                continue
            result = int(result)
            return result
        if typ == 'integer':
            if not result.isdigit():
                continue
            result = int(result)
            if 'min' in kwargs and result < kwargs['min']:
                continue
            if 'max' in kwargs and result > kwargs['max']:
                continue
            return result
    return ""

def find_value_input(user_prompt, value_type, allowed_values, argument_position):
    if len(argv) >= argument_position:
        result = argv[argument_position]
        if value_type == 'integer':
            try:
                result = int(result)
            except Exception as e:
                pass
        if result in allowed_values:
            return result
    result = get_input(user_prompt, typ=value_type,
        kwargs={'min': min(allowed_values), 'max': max(allowed_values)})
    return result