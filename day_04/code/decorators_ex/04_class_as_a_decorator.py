# Using class as a decorator

class decorator2(object):

    def __init__(self, funcobj):
        self.f = funcobj
        print('Decorator creation: ', self.f)

    def __call__(self, arg):
        print("Decorating", self.f.__name__)
        self.f(arg.upper())

@decorator2
def foo(x):
    print("inside foo()", x)

foo('Hello')
