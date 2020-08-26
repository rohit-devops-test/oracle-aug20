Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
>>> 
>>> subprocess.call('dir', shell=True)
0
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle_aug\day_02\code")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_02\\code'
>>> 
>>> 
>>> subprocess.check_output("dir", shell=True)
b' Volume in drive C is Windows\r\n Volume Serial Number is 68CD-4284\r\n\r\n Directory of C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_02\\code\r\n\r\n25-08-2020  17:40    <DIR>          .\r\n25-08-2020  17:40    <DIR>          ..\r\n25-08-2020  11:04               304 01_mult_table_while.py\r\n25-08-2020  11:24             1,282 02_guess_my_number.py\r\n25-08-2020  13:19               161 03_function_args.py\r\n25-08-2020  13:26               294 04_scope_of_vars.py\r\n25-08-2020  13:32               141 05_arg_dtypes.py\r\n25-08-2020  13:38               259 06_var_args.py\r\n25-08-2020  16:14               521 07_generators.py\r\n25-08-2020  12:48               388 primes.py\r\n25-08-2020  13:06               890 project.py\r\n               9 File(s)          4,240 bytes\r\n               2 Dir(s)  308,020,625,408 bytes free\r\n'
>>> c = subprocess.check_output("dir", shell=True)
>>> type(c)
<class 'bytes'>
>>> c[1]
86
>>> c[2]
111
>>> c[3]
108
>>> c[4]
117
>>> print(c)
b' Volume in drive C is Windows\r\n Volume Serial Number is 68CD-4284\r\n\r\n Directory of C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_02\\code\r\n\r\n25-08-2020  17:40    <DIR>          .\r\n25-08-2020  17:40    <DIR>          ..\r\n25-08-2020  11:04               304 01_mult_table_while.py\r\n25-08-2020  11:24             1,282 02_guess_my_number.py\r\n25-08-2020  13:19               161 03_function_args.py\r\n25-08-2020  13:26               294 04_scope_of_vars.py\r\n25-08-2020  13:32               141 05_arg_dtypes.py\r\n25-08-2020  13:38               259 06_var_args.py\r\n25-08-2020  16:14               521 07_generators.py\r\n25-08-2020  12:48               388 primes.py\r\n25-08-2020  13:06               890 project.py\r\n               9 File(s)          4,240 bytes\r\n               2 Dir(s)  308,021,071,872 bytes free\r\n'
>>> c = c.decode()
>>> type(c)
<class 'str'>
>>> c[0]
' '
>>> c[1]
'V'
>>> c[2]
'o'
>>> c[3]
'l'
>>> print(c)
 Volume in drive C is Windows
 Volume Serial Number is 68CD-4284

 Directory of C:\Users\Purushotham\Desktop\oracle_aug\day_02\code

25-08-2020  17:40    <DIR>          .
25-08-2020  17:40    <DIR>          ..
25-08-2020  11:04               304 01_mult_table_while.py
25-08-2020  11:24             1,282 02_guess_my_number.py
25-08-2020  13:19               161 03_function_args.py
25-08-2020  13:26               294 04_scope_of_vars.py
25-08-2020  13:32               141 05_arg_dtypes.py
25-08-2020  13:38               259 06_var_args.py
25-08-2020  16:14               521 07_generators.py
25-08-2020  12:48               388 primes.py
25-08-2020  13:06               890 project.py
               9 File(s)          4,240 bytes
               2 Dir(s)  308,021,071,872 bytes free

>>> type(c)
<class 'str'>
>>> l = c.split('\r\n')
>>> l
[' Volume in drive C is Windows', ' Volume Serial Number is 68CD-4284', '', ' Directory of C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_02\\code', '', '25-08-2020  17:40    <DIR>          .', '25-08-2020  17:40    <DIR>          ..', '25-08-2020  11:04               304 01_mult_table_while.py', '25-08-2020  11:24             1,282 02_guess_my_number.py', '25-08-2020  13:19               161 03_function_args.py', '25-08-2020  13:26               294 04_scope_of_vars.py', '25-08-2020  13:32               141 05_arg_dtypes.py', '25-08-2020  13:38               259 06_var_args.py', '25-08-2020  16:14               521 07_generators.py', '25-08-2020  12:48               388 primes.py', '25-08-2020  13:06               890 project.py', '               9 File(s)          4,240 bytes', '               2 Dir(s)  308,021,071,872 bytes free', '']
>>> l[0]
' Volume in drive C is Windows'
>>> l[1]
' Volume Serial Number is 68CD-4284'
>>> l[2]
''
>>> l[3]
' Directory of C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_02\\code'
>>> 
>>> 
>>> 
>>> 
>>> for line in l:
	if('Volume Serial Number' in line):
		print(line)

		
 Volume Serial Number is 68CD-4284
>>> 
>>> for line in l:
	if(line.endswith('py')):
		print(line)

		
25-08-2020  11:04               304 01_mult_table_while.py
25-08-2020  11:24             1,282 02_guess_my_number.py
25-08-2020  13:19               161 03_function_args.py
25-08-2020  13:26               294 04_scope_of_vars.py
25-08-2020  13:32               141 05_arg_dtypes.py
25-08-2020  13:38               259 06_var_args.py
25-08-2020  16:14               521 07_generators.py
25-08-2020  12:48               388 primes.py
25-08-2020  13:06               890 project.py
>>> l[10]
'25-08-2020  13:26               294 04_scope_of_vars.py'
>>> l[10].split()
['25-08-2020', '13:26', '294', '04_scope_of_vars.py']
>>> 
>>> 
>>> for line in l:
	if(line.endswith('py')):
		data = line.split()
		print(data[-1] + ' -------> ' + str(data[-2]) + ' bytes')

		
01_mult_table_while.py -------> 304 bytes
02_guess_my_number.py -------> 1,282 bytes
03_function_args.py -------> 161 bytes
04_scope_of_vars.py -------> 294 bytes
05_arg_dtypes.py -------> 141 bytes
06_var_args.py -------> 259 bytes
07_generators.py -------> 521 bytes
primes.py -------> 388 bytes
project.py -------> 890 bytes
>>> 
