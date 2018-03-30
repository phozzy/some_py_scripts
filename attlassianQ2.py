with open('input.txt') as inputFile, \
        open('c_programms.txt', 'w') as cFile, \
        open('cpp_programms.txt', 'w') as cppFile, \
        open('cs_programms.txt', 'w') as csFile:
    for it in inputFile:
        {
            'c' : cFile,
            'cpp' : cppFile,
            'cs' : csFile,
        }[it.rstrip().split('.')[1]].write(it)
        # print(it.rstrip().split('.'))
