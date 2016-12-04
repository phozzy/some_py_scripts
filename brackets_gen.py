#!/usb/bin/python3

from functools import reduce
from itertools import repeat

def get_raw_list(level):
    # returns desired level brackets raw list
    return reduce(spawn_brackets, repeat(level, 2 * level - 1), ['('])

def spawn_brackets(accout, itout):
    # spawns brackets branches
    # acc = []
    # for it in accout:
        # opening = it.count('(')
        # closing = it.count(')')
        # acc = acc + (closing < opening) * [it + ')'] + (opening < itout) * [it + '(']
        # if closing < opening: 
            # acc.append(it + ')')
        # if opening < itout:
            # acc.append(it + '(')
    # return acc
    return reduce(lambda acc, it: acc + (it.count(')') < it.count('(')) * [it + ')'] + (it.count('(') < itout) * [it + '('], accout, [])

print(get_raw_list(1))
print(get_raw_list(2))
print(get_raw_list(3))
print(get_raw_list(4))
print(get_raw_list(10))
