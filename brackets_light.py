#!/usr/bin/env python3

from itertools import accumulate

def brackets(level):
    # return filter(lambda it: it.count('1') == level and not(any(block(it))), fmtdrange(level))
    return filter(lambda itera: (lambda it: it.count('1') == level and not(any(block(it))) (bin(itera))), rawrange(level))

def fmtdrange(level):
    return map(lambda x: bin(x).lstrip('0b'), rawrange(level))

def rawrange(level):
    return range(int('0b' + level *'10', base = 2), int('0b' + level * '1' + level * '0', base = 2) + 0b10, 0b10)

def accum_ones(string):
    # return accumulate(map(int, string[::-1]))
    return accumulate(map(int, string.lstrip('0b')[::-1]))

def block(string):
    return map(lambda it: it[1] > it[0] - it[1] + 1 ,enumerate(accum_ones(string)))

def convert_list(lists):
    # convert 1 to ( and 0 to )
    return ''.join(map(lambda it: int(it) and '(' or ')', lists))

for it in brackets(15):
    # print(convert_list(it))
    print(it)
# a = list(brackets(15))
