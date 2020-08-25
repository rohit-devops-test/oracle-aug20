import random


def gendata(n):
    L = []
    for i in range(n):
        L.append(random.randint(1, 100))
    return L

def gendata2(n):
    for i in range(n):
        yield random.randint(1, 100)

x = gendata(10)
print(x)
print(x)
print(x)

print('-'*60)

y = gendata2(10)
print(list(y))
print(list(y))
y = gendata2(10)
print(list(y))

print('-'*60)

y = gendata2(10)
print(next(y))
print(next(y))
print(list(y))

print('-'*60)

for value in gendata2(10):
    print(value, end=' ')
