from functools import reduce

def __compareWords__(accumulator, iterator):
    # returns new accumulator
    return (
        # if length of a new word is even and greater than length of previous accumulator
        (lambda length: (iterator, length) if length % 2 == 0 and length > accumulator[1] else accumulator)
        (len(iterator))
    )

def longestEvenWord(sentence):                    
    # let's go through a list of words from the sentence
    # to find out
    return reduce(
        # result of comparing lengths of words
        __compareWords__,
        sentence.split(),
        # let's initiate zero condition, '00' should be returned if none succeded
        ('00', 0)
    )[0] # result is zero indexed member of tuple
