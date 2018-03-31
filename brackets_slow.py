#!/usr/bin/env python3

from functools import reduce
from itertools import repeat

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, repeat(level, 2 * level - 1), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    # acc = []
    # for it in accout:
        # open_brackets, clos_brackets = it.count('('), it.count(')')
        # (clos_brackets < open_brackets) and acc.append(it + ')')
        # (open_brackets < itout) and acc.append(it + '(')
    # return acc
    return reduce(lambda acc, it:
        (
            (lambda open_brackets, clos_brackets: 
                acc + ((clos_brackets < open_brackets) and [it + ')'] or []) \
                + ((open_brackets < itout) and [it + '('] or [])) 
            (it.count('('), it.count(')'))
        ), 
        accout,
        []
    )

print(get_raw_list(1))
print(get_raw_list(2))
print(get_raw_list(3))
print(get_raw_list(4))
print(len(get_raw_list(12)))
