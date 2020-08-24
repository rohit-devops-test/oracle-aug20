Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 2
>>> c1 = a * b
>>> print(c1)
10
>>> c2 = c1 * c1
>>> print(c2)
100
>>> c3 = c1 * a
>>> c4 = c2 + c3
>>> print(c4)
150
>>> c5 = c4 - (b * b)
>>> print(c5)
146
>>> input('Enter a number: ')
Enter a number: 34
'34'
>>> a = input('Enter a number: ')
Enter a number: 12
>>> print(a)
12
>>> a
'12'
>>> a * 4
'12121212'
>>> type(a)
<class 'str'>
>>> int(a) * 4
48
>>> b = int(input('Enter a number: '))
Enter a number: 34
>>> type(b)
<class 'int'>
>>> b + a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b + a
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> b + int(a)
46
>>> 
=== RESTART: C:\Users\Purushotham\Desktop\oracle_aug\day_01\python_test.py ===
Enter a number: 5
Enter another number: 2
146
>>> 
