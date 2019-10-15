# -*- coding: UTF-8 -*-

def get_sign(prompt='', typ='lowercase', kwargs={}):
    while True:
        result = input(prompt)
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
            if 'max' in kwargs and result < kwargs['max']:
            return result
    return ""

