#!/usr/bin/env python3

from itertools import accumulate

def brackets(level):
    return list(filter(lambda it: it.count('1') == level and not(any(block(it))), fmtdrange(level)))

def fmtdrange(level):
    return map(lambda x: str(bin(x)).lstrip('0b'), rawrange(level))

def rawrange(level):
    return range(int('0b' + level *'10', base = 2), int('0b' + level * '1' + level * '0', base = 2) + 0b10, 0b10)

def accum_ones(string):
    return accumulate(map(int, string[::-1]))

def block(string):
    return map(lambda it: it[1] > it[0] - it[1] + 1 ,enumerate(accum_ones(string)))

for it in brackets(4):
    print(it, list(block(it)))
