Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # NUMBERS
>>> 
>>> # All numeric values
>>> # 5, 1.9, 22/7, -89.008
>>> # Operators
>>> 
>>> # -------------- Arithmetic Operators
>>> 
>>> a = 5
>>> b = 2
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a ** b
25
>>> # ---------------- Relational Operators
>>> 
>>> a > b   # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b
False
>>> a != 2
True
>>> 
>>> a == b ** 2 + 1
True
>>> 
>>> # ----------------- Logical Operators
>>> 
>>> a > b
True
>>> a < 10
True
>>> a > b and a < 10
True
>>> a > b and a > 10
False
>>> a > b or a > 10
True
>>> not(a > b and a > 10)
True
>>> not(a > b) or a < 10
True
>>> 
>>> # IN BUILT FUNCTIONS
>>> 
>>> a = 100
>>> type(a)
<class 'int'>
>>> hex(a)
'0x64'
>>> h = hex(a)
>>> typr(h)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    typr(h)
NameError: name 'typr' is not defined
>>> type(h)
<class 'str'>
>>> bin (a)
'0b1100100'
>>> oct(a)
'0o144'
>>> data = '0b1000101'
>>> type(data)
<class 'str'>
>>> int(data)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(data)
ValueError: invalid literal for int() with base 10: '0b1000101'
>>> int(data, 2)
69
>>> data = '0o144'
>>> int(data)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(data)
ValueError: invalid literal for int() with base 10: '0o144'
>>> int(data, 8)
100
>>> 
>>> s = '1234.456'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '1234.456'
>>> float(s)
1234.456
>>> s = '1234..456'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: '1234..456'
>>> 
>>> a = 5
>>> b = 2
>>> 
>>> a - b
3
>>> b - a
-3
>>> abs(b - a)
3
>>> abs(a - b)
3
>>> File "<pyshell#60>", line 1, in <module>
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> # MODULES
>>> 
>>> 
>>> import math
>>> gcd(111, 55)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    gcd(111, 55)
NameError: name 'gcd' is not defined
>>> math.gcd(111, 55)
1
>>> math.gcd(99, 88)
11
>>> math.sqrt(9)
3.0
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * (22/7)/180)
0.9999998001333682
>>> math.sin(math.radians(90))
1.0
>>> math.sin(90 * math.pi/180)
1.0
>>> 
>>> import random
>>> random.randint(1, 100)
57
>>> random.randint(1, 100)
72
>>> random.randint(1, 100)
83
>>> random.randint(1, 100)
69
>>> random.randint(1, 100)
69
>>> random.randint(1, 100)
13
>>> # ----------------------------------------------------------
>>> 
>>> a = 10
>>> b = math.sqrt(a)
>>> a
10
>>> b
3.1622776601683795
>>> a == b ** 2  # I expect a True here
False
>>> a
10
>>> b
3.1622776601683795
>>> b ** 2
10.000000000000002
>>> 
>>> 
>>> # ------------------------------------------------------------
>>> 
>>> a
10
>>> b
3.1622776601683795
>>> b = 2
>>> a > 2 and a < 10
False
>>> 2 < a < 10  # Chaining of operators
False
>>> 
