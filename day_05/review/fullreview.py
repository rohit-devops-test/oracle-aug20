# Data Types

Numbers - numerical values
Operators - arithmetic, relational, logical,
built-in functions - int(), float(), bin(), oct(), hex(), abs(),
modules - math, random

Strings - collection of characters - "", '', '''  '''
Operators - + * len in del
built-in functions -
case - upper(), lower(), capitalize()
querying - isdigit(), isalpha(), isalnum(), isspace(), startswith(), endswith()
searching - count(), find()
modifications - replace(), split(), join(), strip(), lstrip(), rstrip(), rjust(), ljust()
iteration -> for loop
format()

Lists = ordered collection of objects - []
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
replace L[5] = Value/object
built-in functions
adding values append(), extend(), insert()
removing elements pop(), remove()
searching index(), count()
re-arranging sort(), reverse(), sorted(), reversed()
copying -> deepcopy()
iteration -> for loop
other misc -> max(), min(), sum(), any(), all()

Tuples = ordered collection of objects - () -> immutable list
Operators + * len in del
accessability [start:end:skip] [0] [3:6] [1:10:2]
searching index(), count()
re-arranging sorted(), reversed()
copying -> deepcopy()
iteration -> for loop

Lists/Tuple    x,y,*z = ('red', 'green', 'yellow', 'blue')

Sets = unordered collection - {} -> immutable -> mathematical set theory
Operators | & ^
built-ins -> add(), update(), remove(), intersection(), union()
iteration -> for loop

Dictionaries = unordered collection -> { key:Value }
d[key] = value -> to add a new key value pair
d.setdefault()
d.remove(), d.pop()
d.update()
d.keys(), d.values(), d.items()
iteration -> for loop


# -------------------------------- BRANCHING

if <condition>:
    <statements>
elif <condition>:
    <statements>
..
..
else:
    <statements>


# ------------------------------- LOOPING

for <var> in <iterable>:
    <statements>

while <condition>:
    <statement>

break statement
continue statement

# ------------------------------ FUNCTIONS/MODULES

def <fucntionname>(<arg1>, <arg2> ....):
    <logic>
    return <expr>

# ----------------------------------------------

modules.py -> module/package/library
    <collection of functions>
    def function()
        return <expr>

if __name__ == '__main__':

    <test code>

---------------------------------------

import module
module.function()

# ----------------------------------------------

Special functions: map(), filter(), zip()
Lambda function: fobj = lambda x,y : x + y
Special modules:
datetime -> now(), strftime(), t1 + t2, <format strings>
functools -> reduce()
itertools -> permutation(), combination()
collections -> Counter()
operator -> itemgetter()



# ----------------------------------------------

comprehensions -> [<expr> <loop> <condition>]

exception handling ->
try:
    <statements>
except:
    <statements>
else:
    <statements>
finally:
    <statements>

# ------------------------------------ REGEX

Regular Expressions -> re module -> match(), search(), findall(), finditer()
group(), groups(), groupdict(), span(), start(), end(), sub(), subn()
Metacharacters -> . [abc] [^abc] \ | \d \w \s \D \W \S * + ? {m,n} $ ^ \b \B

www.regex101.com



# -----------------------------------------------------

os -> mkdir(), chdir(), getcwd() .....
os.path -> join(), splitext(), basename() ...
shutil -> move(), copy()
subprocess -> call(), check_output()
csv -> Writer, Reader, DictReader
json -> load(), dump()

# --------------------------------------------------------------------- OOP 

# ----------------------------------------------

OOP - class, object, inheritance, polymorphism, multiple inheritance,

__repr__, __str__, __len__, __iter__, __next__, operator overloading

class class1(object):

    # data items

    # methods

classmodule.py

    class class1(object):

        # data items

        # methods

    class class2(object):

        # data items

        # methods
# -----------------------------------------------------

import classmodule
o1 = classmodule.class1()
o2 = classmodule.class2()

# -----------------------------------------------------------

virtualenv myenv
myenv/Scripts/activate
deactivate

pip freeze > requirements.txt 
pip install -r requirements.txt
pip install modulename
pip uninstall modulename

myapp
    mypackage
        __init__.py   -> import all the functions from the .py module
        a.py
        b.py
    setup.py   -> import setuptools -> setup configuration

cd myapp -> pip install . -> mypackage will be installed globally


# ------------------------------------------------- MISC OOP

decorators
custom exceptions
logging
csv
json
xml

# --------------------------------------------------------------

ORM -> mysql.conenctor connect(), cursor(), execute(), executemany(), fetchall()
Socket -> Server: socket(), bind(), listen(), accept(), send(), receive(), decode(), encode()
          Client: connect()

Multithreading -> threading.Thread
Multitasking -> asyncio
Testing -> unittest.Test
Tkinter -> GUI programming



