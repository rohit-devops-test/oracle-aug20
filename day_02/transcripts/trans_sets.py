Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "mississippi"
>>> 
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 's', 'i', 'p'}
>>> 
>>> s1 = set("abcdefg")
>>> s1
{'a', 'd', 'b', 'g', 'e', 'c', 'f'}
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> # --------------------------------- operators
>>> 
>>> s1
{'a', 'd', 'b', 'g', 'e', 'c', 'f'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> 
>>> s1 | s2
{'a', 'j', 'i', 'd', 'h', 'b', 'g', 'e', 'c', 'f'}
>>> s1 & s2
{'g', 'e', 'f', 'd'}
>>> s1 ^ s2
{'j', 'b', 'a', 'i', 'h', 'c'}
>>> 
>>> 
>>> # --------------------------------- functions
>>> 
>>> s1.add('x')
>>> s1
{'a', 'x', 'd', 'b', 'g', 'e', 'c', 'f'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'a', 'x', 'd', 'y', 'b', 'z', 'g', 'e', 'c', 'f'}
>>> s1.remove('f')
>>> s1
{'a', 'x', 'd', 'y', 'b', 'z', 'g', 'e', 'c'}
>>> 
>>> s1.union(s2)
{'a', 'j', 'x', 'i', 'd', 'h', 'y', 'b', 'z', 'g', 'e', 'c', 'f'}
>>> s1.intersection(s2)
{'g', 'e', 'd'}
>>> 
>>> # ------------------------------ iteration
>>> 
>>> for elem in s1.union(s2):
	print(element, end='-')

	
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    print(element, end='-')
NameError: name 'element' is not defined
>>> for elem in s1.union(s2):
	print(elem, end='-')

	
a-j-x-i-d-h-y-b-z-g-e-c-f-
>>> 
