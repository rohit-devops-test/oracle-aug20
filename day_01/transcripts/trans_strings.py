Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "python"
>>> # "python"
>>> # 'python'
>>> 
>>> type(s)
<class 'str'>
>>> 
>>> # ---------------------- Immutable nature of strings
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ----------------------- subscripting
>>> 
>>> # [index]
>>> # [start:end]
>>> # [start:end:interval]
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[-]1
SyntaxError: invalid syntax
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[1:4] # 1 2 3
'yth'
>>> s[1:5:2] # 1 2 3 4 -> 1 3
'yh'
>>> s[-5:-2]
'yth'
>>> s[-5:-2:2]
'yh'
>>> s[-5:-2:-2]
''
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[4:]
'on'
>>> s[:]
'python'
>>> s[::2]
'pto'
>>> s[1::2]
'yhn'
>>> s[::1]
'python'
>>> s[::-1]
'nohtyp'
>>> s[::-2]
'nhy'
>>> s[-5:-2:-2]
''
>>> s[-5:-2]
'yth'
>>> s[-5:-2][::1]
'yth'
>>> s[-5:-2][::-1]
'hty'
>>> s[-5:-2][::-2]
'hy'
>>> s[-5:-2]
'yth'
>>> s[-5:-2:-1]
''
>>> s[-5:-2][::-1]
'hty'
>>> 
>>> # --------------------------- in-built functions
>>> 
>>> 
>>> 
>>> 
>>> # case related functions
>>> 
>>> 
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> 
>>> # Checking or querying type functions
>>> 
>>> s1 = '123'
>>> s2 = ' '
>>> s3 = 'asd'
>>> s4 = 's343fg'
>>> s5 = '*&^'
>>> 
>>> s1
'123'
>>> int(s1)
123
>>> int(s4)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(s4)
ValueError: invalid literal for int() with base 10: 's343fg'
>>> 
>>> s1.isdigit()
True
>>> if(s1.isdigit()):
	print(int(s1)**2)

	
15129
>>> s3.isdigit()
False
>>> s3.isalpha()
True
>>> s2.isspace()
True
>>> s2.isalpha()
False
>>> s4
's343fg'
>>> s4.isalpha()
False
>>> s4.isalnum()
True
>>> s5.isalnum()
False
>>> s5.isalpha()
False
>>> s3
'asd'
>>> s3.islower()
True
>>> s3.isupper()
False
>>> 
>>> 
>>> site = "www.google.com"
>>> site.startswith("http")
False
>>> site.endswith("com")
True
>>> 
>>> # ------------------------- modification functions
>>> 
>>> ip = "192-90-89-4"
>>> ip.replace('-','.')
'192.90.89.4'
>>> ip
'192-90-89-4'
>>> newip = ip.replace('-','.')
>>> newip
'192.90.89.4'
>>> 
>>> word = '  python  '
>>> word.strip()
'python'
>>> word
'  python  '
>>> word.lstrip()
'python  '
>>> word.rstrip()
'  python'
>>> 
>>> 
>>> w = "carrot"
>>> 
>>> w.ljust(20)
'carrot              '
>>> w.rjust(20, "*")
'**************carrot'
>>> 
>>> text = "python is a powerful language"
>>> text.split()
['python', 'is', 'a', 'powerful', 'language']
>>> text.split('p')
['', 'ython is a ', 'owerful language']
>>> 
>>> words = ['twinkle', 'twinkle', 'little', 'star']
>>> '-'.join(words)
'twinkle-twinkle-little-star'
>>> 
>>> 
>>> # ----------------------------- searching
>>> 
>>> s = "python"
>>> s.find('o')
4
>>> s.find('a')
-1
>>> s.count('y')
1
>>> s = 'reeed'
>>> s.count('e')
3
>>> # OPERATORS
>>> # + * in del len
>>> 
>>> s
'reeed'
>>> len(s)
5
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'python'
>>> 'tho' in s
True
>>> "Python" + "perl"
'Pythonperl'
>>> "Python" * 3
'PythonPythonPython'
>>> 
