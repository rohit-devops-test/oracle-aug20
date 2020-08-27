def getfunc(choice):

    def checkodd(n):
        return n % 2 != 0

    def checkeven(n):
        return n % 2 == 0

    if(choice):
        return checkodd
    else:
        return checkeven

# ------------------------------------------------

f = getfunc(1)
print(f(100), f(101))
