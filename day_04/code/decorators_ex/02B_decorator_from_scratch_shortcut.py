import random

def jumble(funcobj):  # decorator function

    def wrapper(inputstr):  # wrapper function
        L = list(inputstr)
        random.shuffle(L)
        inputword = ''.join(L)
        return funcobj(inputword)

    return wrapper

# modifystring = jumble(modifystring)

@jumble
def modifystring(s):
    return ' '.join([c.upper() for c in s])

@jumble
def changestring(s):
    return s.capitalize()

# -------------------------------------------


print(modifystring('french'))
print(changestring('spanish'))
