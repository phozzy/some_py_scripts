import functools

def __compareWords__(acc, it):
    return (
        (lambda length: (it, length) if length % 2 == 0 and length > acc[1] else acc)
        (len(it))
    )

def longestEvenWord(sentence):                    
    return functools.reduce(
        __compareWords__,
        sentence.split(),
        ('00', 0)
    )[0]
