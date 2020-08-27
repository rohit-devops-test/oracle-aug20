import random


def jumble(funcobj):  # decorator function, funcobj <- modifystring

    def wrapper(inputstr):  # wrapper function, inputstr <- s
        L = list(inputstr)
        random.shuffle(L)
        inputword = ''.join(L)
        return funcobj(inputword)

    return wrapper



def modifystring(s):
    return ' '.join([c.upper() for c in s])

# ---------------------------------------

print(modifystring('apples'))



modifystring = jumble(modifystring)
print('--->', modifystring)


print(modifystring('apples'))  # plaeps


'''

A P P L E S

P L A E P S  <= jumbled up form of the string

'''



# ---------------------------------------------------------


