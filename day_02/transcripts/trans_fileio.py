Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> # Open the file -> open(path, mode)
>>> # mode -> r, w, a
>>> # Closer -> close()
>>> 
>>> # read()
>>> # readline()
>>> # readlines()
>>> 
>>> # tell()
>>> # seek()
>>> 
>>> # write()
>>> # writelines()
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle_july\day_02\examples\lyrics.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_02\examples\lyrics.txt", "r")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle_july\\day_02\\examples\\lyrics.txt' mode='r' encoding='cp1252'>
>>> 
>>> 
>>> print("c:\text\next\space\tab\read.io")
c:	ext
ext\space	abead.io
>>> print(r"c:\text\next\space\tab\read.io")
c:\text\next\space\tab\read.io
>>> \U
SyntaxError: unexpected character after line continuation character
>>> 
>>> 
>>> 
>>> 
>>> # -------------------- reading functions
>>> 
>>> content = f.read()
>>> print(content)
Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people living for today

Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people living life in peace, you

You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one

Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people sharing all the world, you

You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
>>> type(content)
<class 'str'>
>>> 
>>> hist = {}
>>> for ch in content:
	if(ch in hist.keys()):
		hist[ch] = hist[ch] + 1
	else:
		hist[ch] = 1

		
>>> hist
{'I': 15, 'm': 17, 'a': 30, 'g': 13, 'i': 27, 'n': 39, 'e': 58, ' ': 108, 't': 25, 'h': 20, 'r': 24, "'": 10, 's': 23, 'o': 58, 'v': 4, '\n': 26, 'y': 19, 'f': 7, 'u': 16, 'N': 3, 'l': 34, 'b': 5, 'w': 7, 'A': 5, 'k': 2, 'p': 10, 'd': 18, 'c': 3, ',': 2, 'Y': 2, 'B': 2, 'j': 2}
>>> len(hist)
32
>>> 
>>> f.readline()
''
>>> f.tell()
660
>>> len(content)
634
>>> f.seek(0)
0
>>> f.readline()
"Imagine there's no heaven\n"
>>> f.readline()
"It's easy if you try\n"
>>> f.readline()
'No hell below us\n'
>>> f.readline()
'Above us only sky\n'
>>> 
>>> f.seek(0)
0
>>> f.readlines()
["Imagine there's no heaven\n", "It's easy if you try\n", 'No hell below us\n', 'Above us only sky\n', 'Imagine all the people living for today\n', '\n', "Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', '\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> f.seek(0)
0
>>> content = f.readlines()
>>> type(content)
<class 'list'>
>>> content[-1]
'And the world will be as one'
>>> content[::2]
["Imagine there's no heaven\n", 'No hell below us\n', 'Imagine all the people living for today\n', "Imagine there's no countries\n", 'Nothing to kill or die for\n', 'Imagine all the people living life in peace, you\n', "You may say I'm a dreamer\n", "I hope some day you'll join us\n", '\n', 'I wonder if you can\n', 'A brotherhood of man\n', '\n', "But I'm not the only one\n", 'And the world will be as one']
>>> 
>>> f.close()
>>> 
>>> # ------------------------- write into files
>>> 
>>> content
["Imagine there's no heaven\n", "It's easy if you try\n", 'No hell below us\n', 'Above us only sky\n', 'Imagine all the people living for today\n', '\n', "Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', '\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_02\examples\lyrics2.txt", "w")
>>> f.write('Lyrics: Imagine by John Lennon\n')
31
>>> f.write('-'*30+'\n')
31
>>> f.close()
>>> 
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_02\examples\lyrics2.txt", "a")
>>> content = map(lambda s : s.upper(), content)
>>> f.writelines(content)
>>> f.close()
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle_july\day_02\examples\lyrics2.txt", "a")
>>> f.write('-'*30+'\n')
31
>>> f.write('This is a demonstration of file operations in python\n')
53
>>> f.close()
>>> 
