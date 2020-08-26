Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import os.path
>>> import subprocess
>>> import shutil
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle_aug\day_03\os_shutil_subprocess_ex")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex'
>>> 
>>> f = open("data3.txt", "w")
>>> f.close()
>>> 
>>> files = os.listdir()
>>> files
['data1.txt', 'data2.txt', 'data3.txt', 'ipconfig_ex.py', 'road.jpg', 'sunflower.jpg', 'trans_os_shutil.py', 'trans_os_subprocess.py']
>>> 
>>> type(files)
<class 'list'>
>>> 
>>> 
>>> # --------------------------------------
>>> # Create the full paths for each of the files
>>> 
>>> 
>>> path = os.getcwd()
>>> path
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex'
>>> 
>>> fullpaths = []
>>> for file in files:
	fullpaths.append(os.path.join(path, file))

	
>>> fullpaths
['C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data2.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data3.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\ipconfig_ex.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\road.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\sunflower.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_shutil.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_subprocess.py']
>>> 
>>> 
>>> fullpath[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    fullpath[0]
NameError: name 'fullpath' is not defined
>>> fullpaths[0]
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt'
>>> fullpaths[1]
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data2.txt'
>>> 
>>> 
>>> # --------------------------------------------------------
>>> # Create directories according to the file extensions
>>> 
>>> fullpaths[0][-3:]
'txt'
>>> fullpaths[-1][-3:]
'.py'
>>> 
>>> os.path.basename(fullpaths[0])
'data1.txt'
>>> os.path.splitext(os.path.basename(fullpaths[0]))
('data1', '.txt')
>>> os.path.splitext(os.path.basename(fullpaths[0]))[1]
'.txt'
>>> os.path.splitext(os.path.basename(fullpaths[0]))[1][1:]
'txt'
>>> os.path.splitext(os.path.basename(fullpaths[-1]))[1][1:]
'py'
>>> 
>>> 
>>> extlist = []
>>> for path in fullpaths:
	extlist.append(os.path.splitext(os.path.basename(path))[1][1:])

	
>>> extlist
['txt', 'txt', 'txt', 'py', 'jpg', 'jpg', 'py', 'py']
>>> 
>>> set(extlist)
{'txt', 'jpg', 'py'}
>>> 
>>> 
>>> # ------------------------------------ ARUN
>>> 
>>> os.listdir()
['data1.txt', 'data2.txt', 'data3.txt', 'ipconfig_ex.py', 'road.jpg', 'sunflower.jpg', 'text.io.txt', 'trans_os_shutil.py', 'trans_os_subprocess.py']
>>> os.path.splitext('text.io.txt')
('text.io', '.txt')
>>> 
>>> f = open('data4', "w")
>>> f.close()
>>> os.path.splitext('data4')
('data4', '')
>>> 
>>> 
>>> extlist
['txt', 'txt', 'txt', 'py', 'jpg', 'jpg', 'py', 'py']
>>> extlist.append(os.path.splitext('data4')[1])
>>> extlist
['txt', 'txt', 'txt', 'py', 'jpg', 'jpg', 'py', 'py', '']
>>> 
>>> 
>>> set(extlist)
{'', 'txt', 'jpg', 'py'}
>>> 
>>> 
>>> dirlist = ['noext' if dname = '' else dname for dname in set(extlist)]
SyntaxError: invalid syntax
>>> dirlist = ['noext' if dname == '' else dname for dname in set(extlist)]
>>> dirlist
['noext', 'txt', 'jpg', 'py']
>>> 
>>> 
>>> 
>>> # -----------------------------------------------------
>>> # Create directories for each type of extension
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex'
>>> 
>>> for dname in dirlist:
	os.mkdir(dname)

	
>>> os.listdir()
['data1.txt', 'data2.txt', 'data3.txt', 'data4', 'ipconfig_ex.py', 'jpg', 'noext', 'py', 'road.jpg', 'sunflower.jpg', 'text.io.txt', 'trans_os_shutil.py', 'trans_os_subprocess.py', 'txt']
>>> 
>>> 
>>> # ----------------------------------------------------------
>>> # Move the files to respective directories
>>> 
>>> path
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_subprocess.py'
>>> path = os.getcwd()
>>> 
>>> 
>>> fullpaths
['C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data2.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data3.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\ipconfig_ex.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\road.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\sunflower.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_shutil.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_subprocess.py']
>>> for file in os.listdir():
	fullpaths.append(os.path.join(path, file))

	
>>> fullpaths = []
>>> for file in os.listdir():
	fullpaths.append(os.path.join(path, file))

	
>>> fullpaths
['C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data2.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data3.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data4', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\ipconfig_ex.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\noext', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\road.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\sunflower.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\text.io.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_shutil.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\trans_os_subprocess.py', 'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt']
>>> 
>>> os.path.isfile('C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data4')
True
>>> os.path.isfile('C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\py')
False
>>> 
>>> 
>>> src = fullpaths[0]
>>> src
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt'
>>> 
>>> dst = os.path.basename(src)
>>> dst
'data1.txt'
>>> dst = os.path.split(src)
>>> dst
('C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex', 'data1.txt')
>>> ext = os.path.splitext(dst[1])
>>> ext
('data1', '.txt')
>>> fdst = os.path.join(dst[0], ext[1][1:], dst[1])
>>> fdst
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\data1.txt'
>>> src
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data1.txt'
>>> 
>>> shutil.move(src, fdst)
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\data1.txt'
>>> 
>>> 
>>> # ------------------- final logic for moving
>>> 
>>> for path in fullpaths:
	if(os.path.isfile(path)):
		src  = path
		dst  = os.path.split(src)
		ext  = os.path.splitext(dst[1])
		fdst = os.path.join(dst[0], ext[1][1:], dst[1])
		shutil.move(src, fdst)

		
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\data1.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\data2.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\data3.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\data4'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\py\\ipconfig_ex.py'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\jpg\\road.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\jpg\\sunflower.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\txt\\text.io.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\py\\trans_os_shutil.py'
'C:\\Users\\Purushotham\\Desktop\\oracle_aug\\day_03\\os_shutil_subprocess_ex\\py\\trans_os_subprocess.py'
>>> 
