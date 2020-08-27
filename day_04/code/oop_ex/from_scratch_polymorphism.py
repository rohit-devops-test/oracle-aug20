# Polymorphic -> obj.show()


class student:

    def __init__(self):
        pass

    def show(self):
        print('This is student')


class employee:

    def __init__(self):
        pass

    def show(self):
        print('This is employee')


class medical:

    def __init__(self):
        pass

    def show(self):
        print('This is medical')


# -----------------------------------

s = student()
m = medical()
e = employee()

obj = e
obj.show()