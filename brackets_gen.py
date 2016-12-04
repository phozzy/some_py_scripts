#!/usb/bin/python3

from functools import reduce
from itertools import repeat

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, repeat(level, 2 * level - 1), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    return reduce(magic, zip(accout, repeat(itout, len(accout))), [])

def magic(accmagic, itmagic):
    # magic function
    opening = itmagic[0].count('(')
    closing = itmagic[0].count(')')
    return accmagic + (closing < opening) * [itmagic[0] + ')'] + (opening < itmagic[1]) * [itmagic[0] + '(']

print(get_raw_list(1))
print(get_raw_list(2))
print(get_raw_list(3))
print(get_raw_list(4))
# print(get_raw_list(10))
