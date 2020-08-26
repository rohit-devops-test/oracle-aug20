Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> col = 'name,age,regid,phy,chem,math,bio,avg,rank\n'
>>> row = 'Vijay,14,HPE001,99,98,97,96,0,0\n'
>>> 
>>> col = col.split(',')
>>> col
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank\n']
>>> col = [item.strip() for item in col]
>>> col
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank']
>>> row = [item.strip() for item in row.split(',')]
>>> row
['Vijay', '14', 'HPE001', '99', '98', '97', '96', '0', '0']
>>> dict(zip(col, row))
{'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}
>>> cd = {}
>>> cd.setdefault('HPE001', {'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'})
{'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}
>>> 
>>> cd
{'HPE001': {'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '96', 'avg': '0', 'rank': '0'}}
>>> D = {'name': 'Muni', 'age': '14', 'regid': 'HPE003', 'phy': '97', 'chem': '98', 'math': '97', 'bio': '94', 'avg': 96.5, 'rank': 4}
>>> D
{'name': 'Muni', 'age': '14', 'regid': 'HPE003', 'phy': '97', 'chem': '98', 'math': '97', 'bio': '94', 'avg': 96.5, 'rank': 4}
>>> 
>>> 
>>> list(zip(*D.items()))
[('name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank'), ('Muni', '14', 'HPE003', '97', '98', '97', '94', 96.5, 4)]
>>> list(zip(*D.items()))[1]
('Muni', '14', 'HPE003', '97', '98', '97', '94', 96.5, 4)
>>> ','.list(zip(*D.items()))[1] + '\n'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ','.list(zip(*D.items()))[1] + '\n'
AttributeError: 'str' object has no attribute 'list'
>>> ','.[str(s) for s in list(zip(*D.items()))[1]]
SyntaxError: invalid syntax
>>> ','.join([str(s) for s in list(zip(*D.items()))[1]])
'Muni,14,HPE003,97,98,97,94,96.5,4'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> n = 'Anil'
>>> a = 35
>>> 
>>> print('My name is ' + n + 'age is ' + str(a))
My name is Anilage is 35
>>> print('My name is %s and age %d' % (n, a))
My name is Anil and age 35
>>> print('My name is {} and age is {}'.format(n, a))
My name is Anil and age is 35
>>> print('My name is {0} and age is {1}'.format(n, a))
My name is Anil and age is 35
>>> print('My name is {name} and age is {age}'.format(name=n, age=a))
My name is Anil and age is 35
>>> print('My name is {name:20} and age is {age:10}'.format(name=n, age=a))
My name is Anil                 and age is         35
>>> print('My name is {name:>20} and age is {age:<10}'.format(name=n, age=a))
My name is                 Anil and age is 35        
>>> print('My name is {name:^20} and age is {age:^10}'.format(name=n, age=a))
My name is         Anil         and age is     35    
>>> 
>>> 
>>> template = '{name:10} | {age:^20}'
>>> for i in range(5):
	print(template.format(name='Raj', age=a+i))

	
Raj        |          35         
Raj        |          36         
Raj        |          37         
Raj        |          38         
Raj        |          39         
>>> 
