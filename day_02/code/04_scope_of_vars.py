x = 10

def printval(n):
    x = 5
    print(n * x)

def printval2(n):
    global x
    print(n * x)

def printval3(n):
    x = 5
    def func():
        global x
        #nonlocal x
        #x = 1
        print(n * x)
    func()

printval(10)
printval2(10)
printval3(10)
