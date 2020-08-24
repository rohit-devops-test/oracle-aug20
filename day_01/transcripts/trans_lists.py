Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LIST
>>> L = [1, 2, 3, 34.56, 22/7, True, False, "red", "green", "blue"]
>>> L
[1, 2, 3, 34.56, 3.142857142857143, True, False, 'red', 'green', 'blue']
>>> 
>>> # ----------------------- Accesability using sub-scripting
>>> 
>>> L[0]
1
>>> L[1]
2
>>> L[-1]
'blue'
>>> L[-2]
'green'
>>> L[2:5]
[3, 34.56, 3.142857142857143]
>>> L[::2]
[1, 3, 3.142857142857143, False, 'green']
>>> L[::-1]
['blue', 'green', 'red', False, True, 3.142857142857143, 34.56, 3, 2, 1]
>>> L[:4]
[1, 2, 3, 34.56]
>>> L[4:]
[3.142857142857143, True, False, 'red', 'green', 'blue']
>>> 
>>> 
>>> # ------------------- Mutable nature of lists
>>> 
>>> L = ['red', 'green', 'blue']
>>> type(L)
<class 'list'>
>>> L[0]
'red'
>>> L[1]
'green'
>>> L[1] = 'yellow'
>>> L
['red', 'yellow', 'blue']
>>> 
>>> L[1]
'yellow'
>>> L[1][1]
'e'
>>> L[1][1] = 'E'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    L[1][1] = 'E'
TypeError: 'str' object does not support item assignment
>>> # List is mutable, the elements of the list need not be mutable
>>> 
>>> # ------------------------------ Changing values
>>> 
>>> L = ['red', 'green', 'blue']
>>> 
>>> L[1]
'green'
>>> L[1] = ['white', 'black']
>>> L
['red', ['white', 'black'], 'blue']
>>> 
>>> L = ['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1:2]
['green']
>>> L[1:2] = ['white', 'black']
>>> L
['red', 'white', 'black', 'blue']
>>> L
['red', 'white', 'black', 'blue']
>>> L[2:4] = ['maroon', 'cyan', 'magenta']
>>> L
['red', 'white', 'maroon', 'cyan', 'magenta']
>>> 
>>> # -------------------------- Operation done on a list
>>> 
>>> L = ['red', 'green', 'blue']
>>> 
>>> # Adding elements into a list
>>> 
>>> L.append('black')
>>> L
['red', 'green', 'blue', 'black']
>>> L.append('white')
>>> L
['red', 'green', 'blue', 'black', 'white']
>>> L.insert(2, 'yellow')
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white']
>>> L1 = ['magenta', 'cyan']
>>> L.extend(L1)
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta', 'cyan']
>>> 
>>> # Remove elements from a list
>>> 
>>> L.pop()
'cyan'
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta']
>>> L.pop()
'magenta'
>>> L.pop(2)
'yellow'
>>> L
['red', 'green', 'blue', 'black', 'white']
>>> L.remove('blue')
>>> L
['red', 'green', 'black', 'white']
>>> 
>>> # Search elements
>>> 
>>> L = ['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta']
>>> 'black' in L
True
>>> 'apple' in L
False
>>> L.index('red')
0
>>> L.index('black')
4
>>> L.index('apple')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    L.index('apple')
ValueError: 'apple' is not in list
>>> if('apple' in L):
	print(L.index('apple'))

	
>>> L.append('red')
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta', 'red']
>>> L.count('red')
2
>>> 
>>> # Rearranging the elements of a list
>>> 
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x00000234EA590828>
>>> list(reversed(L))
['red', 'magenta', 'white', 'black', 'blue', 'yellow', 'green', 'red']
>>> L
['red', 'green', 'yellow', 'blue', 'black', 'white', 'magenta', 'red']
>>> L.reverse()
>>> L
['red', 'magenta', 'white', 'black', 'blue', 'yellow', 'green', 'red']
>>> 
>>> 
>>> sorted(L)
['black', 'blue', 'green', 'magenta', 'red', 'red', 'white', 'yellow']
>>> L
['red', 'magenta', 'white', 'black', 'blue', 'yellow', 'green', 'red']
>>> L.sort()
>>> L
['black', 'blue', 'green', 'magenta', 'red', 'red', 'white', 'yellow']
>>> L.sort(reverse=True)
>>> 
>>> L
['yellow', 'white', 'red', 'red', 'magenta', 'green', 'blue', 'black']
>>> 
>>> 
>>> # ------------------------- Operators that can act on a list
>>> 
>>> L
['yellow', 'white', 'red', 'red', 'magenta', 'green', 'blue', 'black']
>>> L + ['brown', 'pink']
['yellow', 'white', 'red', 'red', 'magenta', 'green', 'blue', 'black', 'brown', 'pink']
>>> ['brown', 'pink'] * 3
['brown', 'pink', 'brown', 'pink', 'brown', 'pink']
>>> len(L)
8
>>> del L[3]
>>> L
['yellow', 'white', 'red', 'magenta', 'green', 'blue', 'black']
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> L = ['yellow', 'white', 'red', 'red', 'magenta', 'green', 'blue', 'black']
>>> del L[2:5]
>>> L
['yellow', 'white', 'green', 'blue', 'black']
>>> # ---------- Bishwanath
>>> 
>>> # ----------------------------- Copying lists
>>> 
>>> L = ['red', 'green', 'blue']
>>> L1 = L
>>> L
['red', 'green', 'blue']
>>> L1
['red', 'green', 'blue']
>>> L1[1] = 'yellow'
>>> L1
['red', 'yellow', 'blue']
>>> L
['red', 'yellow', 'blue']
>>> 
>>> L = ['red', 'green', 'blue']
>>> L1 = L[:]
>>> L
['red', 'green', 'blue']
>>> L1
['red', 'green', 'blue']
>>> L1[1] = 'yellow'
>>> L
['red', 'green', 'blue']
>>> L1
['red', 'yellow', 'blue']
>>> 
>>> L = ['red', 'green', ['blue', 'yellow']]
>>> L[2][1]
'yellow'
>>> L1 = L
>>> L = ['red', 'green', ['blue', 'yellow']]
>>> L1 = L[:]
>>> L1
['red', 'green', ['blue', 'yellow']]
>>> L
['red', 'green', ['blue', 'yellow']]
>>> L[0] = 'orange'
>>> L
['orange', 'green', ['blue', 'yellow']]
>>> L1
['red', 'green', ['blue', 'yellow']]
>>> L1[2][1] = 'golden'
>>> L1
['red', 'green', ['blue', 'golden']]
>>> L
['orange', 'green', ['blue', 'golden']]
>>> 
>>> 
>>> import copy
>>> L = ['red', 'green', 'blue']
>>> L.append(['yellow', 'orange'])
>>> L
['red', 'green', 'blue', ['yellow', 'orange']]
>>> L1 = copy.deepcopy(L)
>>> L
['red', 'green', 'blue', ['yellow', 'orange']]
>>> L1
['red', 'green', 'blue', ['yellow', 'orange']]
>>> L[0] = 'white'
>>> L
['white', 'green', 'blue', ['yellow', 'orange']]
>>> L1
['red', 'green', 'blue', ['yellow', 'orange']]
>>> L1[-1]
['yellow', 'orange']
>>> L1[-1].append("golden")
>>> L1
['red', 'green', 'blue', ['yellow', 'orange', 'golden']]
>>> L
['white', 'green', 'blue', ['yellow', 'orange']]
>>> 
