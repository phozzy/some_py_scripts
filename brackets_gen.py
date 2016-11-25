#!/usb/bin/python3

from functools import reduce, repeat

def get_level(level):
    # finita
    return filter(lambda it: it.count('(') == level, get_raw_list(level))

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, enumerate(repeat(level, 2 * level)), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    acc = []
    for it in accout:
        if it.count(')') < itout[0]: 
            acc.append(it + ')')
        if it.count('(') < itout[1]:
            acc.append(it + '(')
    return acc
