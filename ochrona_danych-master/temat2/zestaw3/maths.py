# -*- coding: UTF-8 -*-

from random import randint

def greatest_common_divisor(number1, number2):
    a = number1
    b = number2
    while a > 0:
        a, b = b%a, a
    return b

def extended_common_divisor(a, n):
    Gprev = n
    G = a
    Vprev = 0
    V = 1
    i = 1

    while G != 0:
        y = Gprev // G
        G, Gprev = Gprev - y * G, G
        V, Vprev = Vprev - y * V, V
        i += 1

    x = Vprev
    if x >= 0:
        return x
    return x + n

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

def generate_prime(data):
    result = 0
    while result == 0:
        result = random_odd(data)
        if not fermat_test(result, data):
            result = 0
    return result