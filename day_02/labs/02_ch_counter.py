# write a function to accept a string
# return a dictionary of character counts
# Example:  s = 'apples'
# D = {'a':1, 'p':2, 'l':1, 'e':1, 's':1}

def process(s):
    D={}
    for  item in set(s):
        D.setdefault(item,s.count(item))  # Manjeet
        #D[char]=s.count(char) # Rohit

    return D


# --------------------------

if __name__ == "__main__":

    print(process('apples'))
