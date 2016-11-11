from functools import reduce
from operator import or_
from concurrent.futures import ThreadPoolExecutor

def uplevel(brackets):
    # function returns brackets descendants
    return set(map(lambda it: ''.join((brackets[:it], '()', brackets[it:])), range(len(brackets))))
    # length = len(brackets)
    # return set(concurrent.futures.Executor.map(lambda it: ''.join((brackets[:it], '()', brackets[it:])), range(length), None, length))
    # return functools.reduce(lambda acc, it: acc |= ''.join((brackets[:it], '()', brackets[it:])), range(len(brackets)), set())

def getlevel_map(brackets_list):
    # returns map_object of sets of next level brackets
    length = len(brackets_list)
    with ThreadPoolExecutor(length) as executor:
        return executor.map(uplevel, brackets_list)

def getlevel(brackets_list, unused_it = None):
    # returns next level brackets list
    return reduce(or_, getlevel_map(brackets_list))

def return_level(level):
    # function gets required level
    return reduce(getlevel, range(level - 1), {'()'})

print(return_level(1))
print(return_level(2))
print(return_level(3))
print(return_level(4))
print(return_level(9))
