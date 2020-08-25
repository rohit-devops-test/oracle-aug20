Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lambda x, y : x + y
<function <lambda> at 0x0000025559B03620>
>>> # lambda <inputs> : <outputs>
>>> f = lambda x, y: x + y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f("abc", "cdf')
  
SyntaxError: EOL while scanning string literal
>>> f("abc", "cdf")
'abccdf'
>>> f([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> # ----------------------------------- sort function
>>> 
>>> L = ['cat', 'monkey', 'zebra', 'frog']
>>> L.sort()
>>> L
['cat', 'frog', 'monkey', 'zebra']
>>> L.sort(key=lambda s:s[-1])
>>> L
['zebra', 'frog', 'cat', 'monkey']
>>> def sortcriteria(s):
	return s[-1]

>>> L.sort(key=sortcriteria)
>>> L
['zebra', 'frog', 'cat', 'monkey']
>>> 
>>> 
>>> # ---------------------------------- Special functions
>>> 
>>> T = [100, 34, 56, 78, 90]
>>> 
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[212.0, 93.2, 132.8, 172.4, 194.0]
>>> 
>>> F2 = map(lambda t : t * 1.8 + 32, T)
>>> F2
<map object at 0x0000025559AA4A20>
>>> list(F2)
[212.0, 93.2, 132.8, 172.4, 194.0]
>>> 
>>> 
>>> 
>>> L = list(range(100, 200))
>>> L
[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]
>>> 
>>> L1 = []
>>> for n in L:
	if(n % 7 == 0):
		L1.append(n)

		
>>> L1
[105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196]
>>> 
>>> L2 = filter(lambda n : (n % 7 == 0), L)
>>> L2
<filter object at 0x0000025559AA4C18>
>>> list(L2)
[105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196]
>>> 
>>> 
>>> 
>>> 
>>> T1 = ('anil', 'sunil', 'raj')
>>> T2 = ('bangalore', 'mysore', 'coorg')
>>> zip(T1, T2)
<zip object at 0x000002555986ED48>
>>> list(zip(T1, T2))
[('anil', 'bangalore'), ('sunil', 'mysore'), ('raj', 'coorg')]
>>> 
>>> D = {'name':'anil', 'age':35, 'country', 'India' }
SyntaxError: invalid syntax
>>> D = {'name':'anil', 'age':35, 'country': 'India'
     }
>>> D
{'name': 'anil', 'age': 35, 'country': 'India'}
>>> D.items()
dict_items([('name', 'anil'), ('age', 35), ('country', 'India')])
>>> zip(*D.items())
<zip object at 0x0000025559B2FDC8>
>>> list(zip(*D.items()))
[('name', 'age', 'country'), ('anil', 35, 'India')]
>>> 
>>> 
>>> # ------------------------ special functions from other builtin modules
>>> 
>>> from functools import reduce
>>> L = [1,2,3,4]
>>> reduce(lambda x,y : x+y, L)
10
>>> L = ['red', 'green', 'blue']
>>> reduce(lambda x,y:x*3+x*3, L)
'redredredredredredredredredredredredredredredredredredredredredredredredredredredredredredredredredredredred'
>>> reduce(lambda x,y:x*3+y*3, L)
'redredredgreengreengreenredredredgreengreengreenredredredgreengreengreenblueblueblue'
>>> L = ['red', 'green', 'blue']
>>> ''.join(L)
'redgreenblue'
>>> reduce(lambda x,y:x+y, L)
'redgreenblue'
>>> 
>>> 
>>> 
>>> from itertools import permutations, combinations
>>> L = ['a', 'b', 'c', 'd']
>>> permutations(L, 3)
<itertools.permutations object at 0x0000025559AEDE60>
>>> list(permutations(L, 3))
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'b'), ('a', 'c', 'd'), ('a', 'd', 'b'), ('a', 'd', 'c'), ('b', 'a', 'c'), ('b', 'a', 'd'), ('b', 'c', 'a'), ('b', 'c', 'd'), ('b', 'd', 'a'), ('b', 'd', 'c'), ('c', 'a', 'b'), ('c', 'a', 'd'), ('c', 'b', 'a'), ('c', 'b', 'd'), ('c', 'd', 'a'), ('c', 'd', 'b'), ('d', 'a', 'b'), ('d', 'a', 'c'), ('d', 'b', 'a'), ('d', 'b', 'c'), ('d', 'c', 'a'), ('d', 'c', 'b')]
>>> for perm in permutations(L, 3):
	print(''.join(perm), end=' ')

	
abc abd acb acd adb adc bac bad bca bcd bda bdc cab cad cba cbd cda cdb dab dac dba dbc dca dcb 
>>> for perm in permutations(L, 2):
	print(''.join(perm), end=' ')

	
ab ac ad ba bc bd ca cb cd da db dc 
>>> for perm in combinations(L, 3):
	print(''.join(perm), end=' ')

	
abc abd acd bcd 
>>> 
>>> 
>>> from collections import Counter
>>> L = ['red', 'red', 'blue', 'green']
>>> D = {}
>>> for item in set(L):
	D.setdefault(item, L.count(item))

	
1
2
1
>>> D
{'green': 1, 'red': 2, 'blue': 1}
>>> z = Counter(L)
>>> z
Counter({'red': 2, 'blue': 1, 'green': 1})
>>> 
>>> 
>>> 
>>> 
>>> from operator import itemgetter
>>> itemgetter(1)("apples")
'p'
>>> itemgetter(1)(["red", "green", "blue"])
'green'
>>> getfirst = itemgetter(1)
>>> type(getfirst)
<class 'operator.itemgetter'>
>>> 
>>> 
>>> getfirst("mango")
'a'
>>> getfirst(["red", "green", "blue"])
'green'
>>> L = ['cat', 'monkey', 'zebra', 'frog']
>>> L.sort(key=getfirst)
>>> L
['cat', 'zebra', 'monkey', 'frog']
>>> 
>>> 
>>> 
>>> 
>>> from datetime import datetime
>>> 
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 8, 25, 15, 52, 26, 818488)
>>> t.year
2020
>>> t.month
8
>>> t.day
25
>>> t.hour
15
>>> t.minute
52
>>> t.second
26
>>> t1 = datatime.now()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    t1 = datatime.now()
NameError: name 'datatime' is not defined
>>> t1 = datetime.now()
>>> t1 - t
datetime.timedelta(seconds=104, microseconds=242130)
>>> f = "%A, %d %B %Y, %I:%M:%S %p"
>>> t.strftime(f)
'Tuesday, 25 August 2020, 03:52:26 PM'
>>> t
datetime.datetime(2020, 8, 25, 15, 52, 26, 818488)
>>> 
