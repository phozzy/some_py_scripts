#!/usb/bin/python3

from functools import reduce
from itertools import repeat

def get_level(level):
    # finita
    return filter(lambda it: it.count('(') == level, get_raw_list(level))

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, enumerate(repeat(level, 2 * level - 1)), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    acc = []
    for it in accout:
        opening = it.count('(')
        closing = it.count(')')
        if closing < opening: 
            acc.append(it + ')')
        if opening < itout[1]:
            acc.append(it + '(')
    return acc

print(get_raw_list(12))
# print(get_raw_list(2))
# print(get_raw_list(3))
# print(get_raw_list(4))
# print(get_raw_list(5))
