Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ("red", "green", "blue")
>>> 
>>> # --------------------- accessing and immutability
>>> 
>>> T[0]
'red'
>>> T[-1]
'blue'
>>> T[1:3]
('green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> 
>>> T[0] = "orange"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    T[0] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # --------------------- rearrangement and searching
>>> 
>>> T
('red', 'green', 'blue')
>>> sorted(T)
['blue', 'green', 'red']
>>> reversed(T)
<reversed object at 0x000001F7ABD32A58>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> 
>>> T.count("red")
1
>>> T.index("red")
0
>>> # ----------------------- operators
>>> 
>>> T1 = ("white", "black")
>>> T + T1
('red', 'green', 'blue', 'white', 'black')
>>> T
('red', 'green', 'blue')
>>> T1
('white', 'black')
>>> 
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> len(T)
3
>>> "red" in T
True
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T1
>>> T1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> 
>>> # ---------------------------------- iterated
>>> 
>>> for color in T:
	print(color.upper())

	
RED
GREEN
BLUE
>>> 
>>> # ----------------------------------- specials
>>> 
>>> r,g,b = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> T2 = ('red', 'green', 'blue', 'white', 'black')
>>> r,g,b = T2
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    r,g,b = T2
ValueError: too many values to unpack (expected 3)
>>> r,g,b,*x = T2
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> x
['white', 'black']
>>> r,g,b = T2[:3]
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> *y = T2
SyntaxError: starred assignment target must be in a list or tuple
>>> T2
('red', 'green', 'blue', 'white', 'black')
>>> x, *y = T2
>>> x
'red'
>>> y
['green', 'blue', 'white', 'black']
>>> 
