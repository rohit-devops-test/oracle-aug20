C:\Users\Purushotham\Desktop\oracle_aug\day_04\code\oop_ex>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from employee import Emploee
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'Emploee' from 'employee' (C:\Users\Purushotham\Desktop\oracle_aug\day_04\code\oop_ex\employee.py)
>>> from employee import Employee
>>> e = Employee('Anil', 'Oracle', '1000000 USD')
>>> e
Anil Oracle 1000000 USD
>>> print(e)
Anil Oracle 1000000 USD
>>> len(e)
1
>>> L = []
>>> for i in range(10):
...     L.append(Employee('Anil', 'Oracle', str(100000 * (i + 1)) + ' USD'))
...
>>> L
[Anil Oracle 100000 USD, Anil Oracle 200000 USD, Anil Oracle 300000 USD, Anil Oracle 400000 USD, Anil Oracle 500000 USD, Anil Oracle 600000 USD, Anil Oracle 700000 USD, Anil Oracle 800000 USD, Anil Oracle 900000 USD, Anil Oracle 1000000 USD]
>>> for obj in L:
...     obj.printinfo()
... 
ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 100000 USD       
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 200000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 300000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 400000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 500000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 600000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 700000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 800000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 900000 USD
TAX        : 0



ANIL
------------------------------
COMPANY    : Oracle
SALARY     : 1000000 USD
TAX        : 0



>>> for obj in L:
...     print(obj)
... 
Anil Oracle 100000 USD
Anil Oracle 200000 USD
Anil Oracle 300000 USD
Anil Oracle 400000 USD
Anil Oracle 500000 USD
Anil Oracle 600000 USD
Anil Oracle 700000 USD
Anil Oracle 800000 USD
Anil Oracle 900000 USD
Anil Oracle 1000000 USD
>>>
>>> len(e)
11
>>> len(Employee)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'type' has no len()
>>> len(e)
11
>>>
