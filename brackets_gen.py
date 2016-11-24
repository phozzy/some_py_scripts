#!/usb/bin/python3

from functools import reduce, repeat

def get_level(level):
    # finita
    return filter(lambda it: it.count('(') == level, get_raw_list(level))

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, enumerate(repeat(level, 2 * level)), ['('])

def spawn_brackets(acc, itout):
    # spawns brackets branches
