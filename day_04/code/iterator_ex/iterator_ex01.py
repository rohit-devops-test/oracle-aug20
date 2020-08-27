class MyNumbers:

    def __init__(self, max):
        self.maxlimit = max
        self.a = 0

    def __str__(self):
        return 'This is object of MyNumbers'

    def __repr__(self):
        return 'MyNumber Object with maximum limit ' + str(self.maxlimit)

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.maxlimit:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers(15)
#myiter = iter(myclass)


print(myclass)

for x in myclass:
  print(x)
