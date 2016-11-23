#!/usb/bin/python3

from functools import reduce

def get_level(level):
    # finita
    return filter(lambda it: it.count('(') == level, get_raw_list(level))

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, range(2 * level), ['('])

def spawn_brackets(acc, it):
    # spawns brackets branches
