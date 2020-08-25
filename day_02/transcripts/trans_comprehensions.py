Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = []
>>> for i in range(1, 11):
	t = (i, i**2, i**3)
	L.append(t)

	
>>> L
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> LC = [(x, x**2, x**3) for x in range(1, 11)]
>>> LC
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> 
>>> # Syntax
>>> # [] {} ()
>>> # [<expr> <loop> <condition>]
>>> 
>>> LC = [x**2 for x in range(1, 101) if x % 7 == 0]
>>> LC
[49, 196, 441, 784, 1225, 1764, 2401, 3136, 3969, 4900, 5929, 7056, 8281, 9604]
>>> 
>>> s = ["red", "green", "blue"]
>>> DC = {x:len(x) for x in s}
>>> Dc
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Dc
NameError: name 'Dc' is not defined
>>> DC
{'red': 3, 'green': 5, 'blue': 4}
>>> DC = {x:{length:len(x), hist:Counter(x)} for x in s}
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    DC = {x:{length:len(x), hist:Counter(x)} for x in s}
  File "<pyshell#22>", line 1, in <dictcomp>
    DC = {x:{length:len(x), hist:Counter(x)} for x in s}
NameError: name 'length' is not defined
>>> from collections import Counter
>>> DC = {x:{'length':len(x), 'hist':Counter(x)} for x in s}
>>> DC
{'red': {'length': 3, 'hist': Counter({'r': 1, 'e': 1, 'd': 1})}, 'green': {'length': 5, 'hist': Counter({'e': 2, 'g': 1, 'r': 1, 'n': 1})}, 'blue': {'length': 4, 'hist': Counter({'b': 1, 'l': 1, 'u': 1, 'e': 1})}}
>>> 
>>> 
>>> 
>>> T = (1, 2, 3, 4)
>>> TC = (x**2 for x in T if x == 3)
>>> TC
<generator object <genexpr> at 0x0000010DA6CDB9A8>
>>> list(TC)
[9]
>>> TC = (x**2 if x == 3 else x for x in T)
>>> list(TC)
[1, 2, 9, 4]
>>> 
