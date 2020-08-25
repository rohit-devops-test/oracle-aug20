Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['Raj', 35, 'Oracle', 'India']
>>> L.insert(2, "23-05-77")
>>> L
['Raj', 35, '23-05-77', 'Oracle', 'India']
>>> 
>>> D = {'name':'Raj', 'age':35, 'company':'Oracle', 'country':'India'}
>>> D['name']
'Raj'
>>> D['age']
35
>>> D['dob'] = "23-05-77"
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77'}
>>> 
>>> # ------------------------------- operations
>>> 
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77'}
>>> D['name']
'Raj'
>>> D['salary']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    D['salary']
KeyError: 'salary'
>>> D['salary'] = '1000000 INR'
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '1000000 INR'}
>>> D['salary'] = '2000000 INR'
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR'}
>>> 
>>> D.setdefault('salary')
'2000000 INR'
>>> D.setdefault('addr')
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'addr': None}
>>> D.setdefault('addr', 'Bangalore')
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'addr': None}
>>> D.setdefault('addr')
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'addr': None}
>>> D.setdefault('addr', 'Bangalore')
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'addr': None}
>>> D.setdefault('hometown', 'Bangalore')
'Bangalore'
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'addr': None, 'hometown': 'Bangalore'}
>>> D.setdefault('hometown')
'Bangalore'
>>> 
>>> D.pop('addr')
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'hometown': 'Bangalore'}
>>> 
>>> 
>>> D1 = {'hobby':'music', 'married': 'N' }
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'hometown': 'Bangalore'}
>>> D.update(D1)
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'hometown': 'Bangalore', 'hobby': 'music', 'married': 'N'}
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'age', 'company', 'country', 'dob', 'salary', 'hometown', 'hobby', 'married'])
>>> D.values()
dict_values(['Raj', 35, 'Oracle', 'India', '23-05-77', '2000000 INR', 'Bangalore', 'music', 'N'])
>>> D.items()
dict_items([('name', 'Raj'), ('age', 35), ('company', 'Oracle'), ('country', 'India'), ('dob', '23-05-77'), ('salary', '2000000 INR'), ('hometown', 'Bangalore'), ('hobby', 'music'), ('married', 'N')])
>>> 
>>> 
>>> # ------------------------------------- iterations
>>> 
>>> 
>>> for key in D:
	print(key)

	
name
age
company
country
dob
salary
hometown
hobby
married
>>> for key in D.keys():
	print(key)

	
name
age
company
country
dob
salary
hometown
hobby
married
>>> for value in D.values():
	print(value)

	
Raj
35
Oracle
India
23-05-77
2000000 INR
Bangalore
music
N
>>> 
>>> for item in D.items():
	print(item)

	
('name', 'Raj')
('age', 35)
('company', 'Oracle')
('country', 'India')
('dob', '23-05-77')
('salary', '2000000 INR')
('hometown', 'Bangalore')
('hobby', 'music')
('married', 'N')
>>> 
>>> for key, value in D.items():
	print(key + ' ----> ' + str(value))

	
name ----> Raj
age ----> 35
company ----> Oracle
country ----> India
dob ----> 23-05-77
salary ----> 2000000 INR
hometown ----> Bangalore
hobby ----> music
married ----> N
>>> 
>>> D
{'name': 'Raj', 'age': 35, 'company': 'Oracle', 'country': 'India', 'dob': '23-05-77', 'salary': '2000000 INR', 'hometown': 'Bangalore', 'hobby': 'music', 'married': 'N'}
>>> 
>>> DN = {}
>>> for key, value in D.items():
	DN.setdefault(value, key)

	
'name'
'age'
'company'
'country'
'dob'
'salary'
'hometown'
'hobby'
'married'
>>> DN
{'Raj': 'name', 35: 'age', 'Oracle': 'company', 'India': 'country', '23-05-77': 'dob', '2000000 INR': 'salary', 'Bangalore': 'hometown', 'music': 'hobby', 'N': 'married'}
>>> 
