Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> L = ['red', 'green', 'blue', 'yellow']
>>> 
>>> for ch in s:
	print('Oracle')

	
Oracle
Oracle
Oracle
Oracle
Oracle
Oracle
>>> for ch in s:
	print(ch, 'Oracle')

	
p Oracle
y Oracle
t Oracle
h Oracle
o Oracle
n Oracle
>>> i = 1
>>> for ch in s:
	print(ch, 'Oracle' * i)
	i = i + 1

	
p Oracle
y OracleOracle
t OracleOracleOracle
h OracleOracleOracleOracle
o OracleOracleOracleOracleOracle
n OracleOracleOracleOracleOracleOracle
>>> for item in L:
	print(item + ' ---> ' + str(len(item)))

	
red ---> 3
green ---> 5
blue ---> 4
yellow ---> 6
>>> 
>>> # 5 X 1 = 5
>>> N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))
5 X 1 = 5
>>> for i in N:
	print(str(5) + ' X ' + str(1) + ' = ' + str(5 * 1))

	
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
>>> for i in N:
	print(str(5) + ' X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(10, 100, 5))
[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> for i in range(1, 11):
	print(str(5) + ' X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle_aug/day_01/code/02_mult_table.py 
Enter a number: 
	for i in range(1, 11):
		print(str(5) + ' X ' + str(i) + ' = ' + str(5 * i))
