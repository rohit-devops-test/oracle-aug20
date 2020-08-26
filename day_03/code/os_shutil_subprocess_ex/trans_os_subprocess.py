Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import os.path
>>> import subprocess
>>> import shutil
>>> 
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> path = r"C:\Users\Purushotham\Desktop\oracle-june\day_05\os_shutil_subprocess_ex"
>>> os.chdir(path)
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex'
>>> os.listdir()
['road.jpg', 'sunflower.jpg']
>>> f = open('data1.txt', "w")
>>> f.write('Hello Oracle')
12
>>> f.close()
>>> os.listdir()
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> files = os.listdir()
>>> file
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    file
NameError: name 'file' is not defined
>>> files
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> paths  = []
>>> for file in files:
	paths.append(os.path.join(path, file))

	
>>> paths
['C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\data1.txt', 'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\road.jpg', 'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\sunflower.jpg']
>>> path[0]
'C'
>>> paths[0]
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\data1.txt'
>>> os.path.basename(path[0])
'C'
>>> os.path.basename(paths[0])
'data1.txt'
>>> os.path.splitext(os.path.basename(paths[0]))
('data1', '.txt')
>>> os.path.splitext(os.path.basename(paths[0]))[1:]
('.txt',)
>>> os.path.splitext(os.path.basename(paths[0]))[1]
'.txt'
>>> os.path.splitext(os.path.basename(paths[0]))[1][1:]
'txt'
>>> # ----------------------------------------
>>> 
>>> 
>>> os.listdir()
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> for file in os.listdir():
	print(file[-3:])

	
txt
jpg
jpg
>>> for file in os.listdir():
	os.path.splitext(file)[1:]

	
('.txt',)
('.jpg',)
('.jpg',)
>>> for file in os.listdir():
	os.path.splitext(file)[1][1:]

	
'txt'
'jpg'
'jpg'
>>> dirs = []
>>> for file in os.listdir():
	dirs.append(os.path.splitext(file)[1][1:])

	
>>> dirs
['txt', 'jpg', 'jpg']
>>> set(dirs)
{'txt', 'jpg'}
>>> dirs = list(set(dirs))
>>> dirs
['txt', 'jpg']
>>> 
>>> 
>>> for d in dirs:
	os.mkdir(d)

	
>>> files
['data1.txt', 'road.jpg', 'sunflower.jpg']
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex'
>>> for file in files:
	dirname = os.path.splitext(file)[1][1:]
	dest = os.path.join(os.getcwd(), dirname)
	shutil.move(file, os.path.join(dest, file))

	
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\txt\\data1.txt'
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\jpg\\road.jpg'
'C:\\Users\\Purushotham\\Desktop\\oracle-june\\day_05\\os_shutil_subprocess_ex\\jpg\\sunflower.jpg'
>>> 
