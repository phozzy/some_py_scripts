def longestEvenWord(sentence):                    
    return functools.reduce(lambda acc, it: ((lambda length: (it, length) if length % 2 == 0 and length > acc[1] else acc)(len(it))), sentence.split(), ('00', 0))
