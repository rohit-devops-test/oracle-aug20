# Refer: https://docs.python.org/3/library/operator.html
# For a complete set of operators that can be overloaded in python

class complex:

    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    def __str__(self):
        return str(self.real) + ' + j' +  str(self.imaginary)

    def __add__(self, other):     # oa + ob   ====> self + other
        return complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):     # oa - ob   ====> self + other
        return complex(self.real - other.real, self.imaginary - other.imaginary)

    def __floordiv__(self, other): # oa // ob
        <logic>
        return complex()




oa = complex(5, 12)
ob = complex(7, 8)
print(oa)
print(ob)


oc = oa + ob
print(oc)

od = oa - ob
print(od)
