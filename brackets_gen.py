#!/usr/bin/env python3

from functools import reduce
from itertools import repeat

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, repeat(level, 2 * level - 1), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    acc = []
    for it in accout:
        open_brackets, clos_brackets = it.count('('), it.count(')')
        acc += (clos_brackets < open_brackets) * [it + ')']
        acc += (open_brackets < itout) * [it + '(']
    return acc

print(get_raw_list(1))
print(get_raw_list(2))
print(get_raw_list(3))
print(get_raw_list(4))
print(len(get_raw_list(15)))
