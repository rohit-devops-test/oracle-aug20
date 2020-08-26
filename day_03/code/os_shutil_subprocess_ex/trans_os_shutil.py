Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import os.path
>>> import subprocess
>>> import shutil
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex'
>>> os.listdir()
['ipconfig_ex.py', 'road.jpg', 'sunflower.jpg', 'trans_os_subprocess.py', '__pycache__']
>>> 
>>> 
>>> f = open("data1.txt", "w")
>>> f.close()
>>> f = open("data2.txt", "w")
>>> f.close()
>>> 
>>> 
>>> files = os.listdir()
>>> files
['data1.txt', 'data2.txt', 'ipconfig_ex.py', 'road.jpg', 'sunflower.jpg', 'trans_os_subprocess.py', '__pycache__']
>>> 
>>> 
>>> 
>>> # -----------------------------------------------------
>>> 
>>> # Creating full paths for each of the files
>>> 
>>> path = os.getcwd()
>>> path
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex'
>>> for file in files:
	print(os.path.join(path, file))

	
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\data1.txt
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\data2.txt
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\ipconfig_ex.py
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\road.jpg
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\sunflower.jpg
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\trans_os_subprocess.py
C:\Users\Purushotham\Desktop\oracle_july\day_04\session_01\os_shutil_subprocess_ex\__pycache__
>>> 
>>> 
>>> fullpaths = []
>>> for file in files:
	fullpaths.append(os.path.join(path, file))

	
>>> fullpaths[0]
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> fullpaths[0][-3:]
'txt'
>>> fullpath[0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    fullpath[0]
NameError: name 'fullpath' is not defined
>>> fullpaths[0]
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> os.path.basename(fullpath[0])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    os.path.basename(fullpath[0])
NameError: name 'fullpath' is not defined
>>> os.path.basename(fullpaths[0])
'data1.txt'
>>> os.path.splitext(os.path.basename(fullpaths[0]))
('data1', '.txt')
>>> os.path.splitext(os.path.basename(fullpaths[0]))[1]
'.txt'
>>> os.path.splitext(os.path.basename(fullpaths[0]))[1][1:]
'txt'
>>> 
>>> # --------------------------------------------------------------------
>>> 
>>> extlist = []
>>> for path in fullpaths:
	extlist.append(os.path.splitext(os.path.basename(fullpaths[0]))[1][1:])

	
>>> extlist
['txt', 'txt', 'txt', 'txt', 'txt', 'txt', 'txt']
>>> extlist = []
>>> for path in fullpaths:
	extlist.append(os.path.splitext(os.path.basename(path))[1][1:])

	
>>> extlist
['txt', 'txt', 'py', 'jpg', 'jpg', 'py', '']
>>> fullpaths
['C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data2.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\ipconfig_ex.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\road.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\sunflower.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\trans_os_subprocess.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\__pycache__']
>>> fullpaths[0]
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> 
>>> 
>>> dirlist = list(set(extlist))
>>> dirlist
['jpg', '', 'txt', 'py']
>>> 
>>> 
>>> ######### Use a comprehension to clean up the list
>>> 
>>> dirlistfinal = ['noext' if dname = '' else dname for dname in dirlist]
SyntaxError: invalid syntax
>>> dirlistfinal = ['noext' if dname == '' else dname for dname in dirlist]
>>> dirlistfinal
['jpg', 'noext', 'txt', 'py']
>>> 
>>> 
>>> # --------------------- Create the dicrtories
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex'
>>> for d in dirlistfinal:
	os.mkdir(d)

	
>>> os.listdir()
['data1.txt', 'data2.txt', 'ipconfig_ex.py', 'jpg', 'noext', 'py', 'road.jpg', 'sunflower.jpg', 'trans_os_subprocess.py', 'txt']
>>> 
>>> # ----------------------- Move the files
>>> 
>>> src = fullpaths[0]
>>> scr
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    scr
NameError: name 'scr' is not defined
>>> src
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> os.path.splitext(os.path.basename(path))[1][1:]
''
>>> os.path.splitext(os.path.basename(src))[1][1:]
'txt'
>>> os.path.basename(src)
'data1.txt'
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex'
>>> 
>>> 
>>> dest = os.path.join(os.getcwd() + os.path.splitext(os.path.basename(src))[1][1:] + os.path.basename(src))
>>> dest
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_extxtdata1.txt'
>>> dest = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(src))[1][1:], os.path.basename(src))
>>> dest
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt\\data1.txt'
>>> src
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> shuil.move(src, dest)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    shuil.move(src, dest)
NameError: name 'shuil' is not defined
>>> shutil.move(src, dest)
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt\\data1.txt'
>>> os.chdir(txt)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    os.chdir(txt)
NameError: name 'txt' is not defined
>>> os.chdir('txt')
>>> os.listdir()
['data1.txt']
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt'
>>> os.chdir(os.pardir)
>>> os.listdir()
['data2.txt', 'ipconfig_ex.py', 'jpg', 'noext', 'py', 'road.jpg', 'sunflower.jpg', 'trans_os_subprocess.py', 'txt']
>>> 
>>> 
>>> for path in fullpaths:
	dest = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(path))[1][1:], os.path.basename(path))
	shutil.move(path, dest)

	
Traceback (most recent call last):
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 563, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt' -> 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt\\data1.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#109>", line 3, in <module>
    shutil.move(path, dest)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 577, in move
    copy_function(src, real_dst)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 263, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\data1.txt'
>>> for path in fullpaths:
	dest = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(path))[1][1:], os.path.basename(path))
	shutil.move(path, dest)

	
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt\\data1.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\txt\\data2.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\py\\ipconfig_ex.py'
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\jpg\\road.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\jpg\\sunflower.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\py\\trans_os_subprocess.py'
Traceback (most recent call last):
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 563, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\__pycache__' -> 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\__pycache__'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#111>", line 3, in <module>
    shutil.move(path, dest)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 577, in move
    copy_function(src, real_dst)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 263, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_04\\session_01\\os_shutil_subprocess_ex\\__pycache__'
>>> 
>>> 
>>> # ------------------------ Note
>>> 
>>> # To remove the above error, use the isfile() to check if the path is a file
>>> # and then invoke the shutil.move()
>>> 
>>> 
