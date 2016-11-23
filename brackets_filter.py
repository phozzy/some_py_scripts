#!/usr/bin/python3

from itertools import product, accumulate
#from concurrent.futures import ProcessPoolExecutor

def gen_raw_product(level):
    # generate raw product of 0 and 1
    return filter(lambda it: it[0] == '0' and it[-1] == '1', product('01', repeat = 2 * level))

def conver2integers(lists):
    # conver 0 and 1 to integers
    return list(map(int, lists))

def conv_int_product(level):
    # conver to integers
    # with ProcessPoolExecutor() as executor:
        # return executor.map(conver2integers, gen_raw_product(level))
    return map(conver2integers, gen_raw_product(level))

def filter_by_level(level):
    # filter by sum
    return filter(lambda it: sum(it) == level, conv_int_product(level))

def filter_rule(lists):
    # filter rule for lists
    return all(map(lambda it: it[0] < 2 or it[1] <= it[0] - it[1] + 1, enumerate(accumulate(lists))))

def raw_final(level):
    # get raw final list
    return filter(filter_rule, filter_by_level(level))

def convert_list(lists):
    # convert 0 to ( and 1 to )
    return ''.join(map(lambda it: it and ')' or '(', lists))

def convert2string(level):
    # convert to strings
    # with ProcessPoolExecutor() as executor:
        # return executor.map(convert_list, raw_final(level))
    return map(convert_list, raw_final(level))

print(list(convert2string(1)))
print(list(convert2string(2)))
print(list(convert2string(3)))
print(list(convert2string(4)))
print(list(convert2string(5)))
