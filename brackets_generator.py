#!/usr/bin/env python3

from itertools import accumulate
# uncomment this for random range, comment for straight range
# from random import randrange

def brackets(level):
    # return filter(lambda it: it.count('1') == level and not(any(block(it))), fmtdrange(level))
    # return filter(lambda itera: (lambda it: it.count('1') == level and not(any(block(it))) (bin(itera))), rawrange(level))
    return filter(lambda it: bin(it).count('1') == level and vodoo(it, level), rawrange(level))

def fmtdrange(level):
    return map(lambda x: bin(x).lstrip('0b'), rawrange(level))

def rawrange(level):
    # comment this for random range, uncomment for straight range
    return range(startvalue(level), stopvalue(level), 2)
    # uncomment this for random range, comment for straight range
    # return randrange(startvalue(level), stopvalue(level), 2)

def startvalue(level):
    # returns start value of sequence
    return sum(map(lambda it: 2 ** (2 * it + 1), range(level)))

def stopvalue(level):
    # returns end of the range
    return 2 ** (2 * level) - 2 ** level + 2

def accum_ones(string):
    return accumulate(map(int, string[::-1]))
    # return accumulate(map(int, string.lstrip('0b')[::-1]))

def block(string):
    return map(lambda it: it[1] > it[0] - it[1] + 1 ,enumerate(accum_ones(string)))

def vodoo(value, level):
    return not(any(map(lambda it: (value % (2 ** (it * 2 + 1))) >= (2 ** (2 * it + 1) - 2 ** it), range(1, level))))

def convert_list(lists):
    # convert 1 to ( and 0 to )
    return ''.join(map(lambda it: int(it) and '(' or ')', lists))

for it in brackets(15):
    # print(convert_list(bin(it).lstrip('0b')))
    print(it)
# a = list(brackets(15))
