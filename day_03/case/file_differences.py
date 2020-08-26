import difflib
from pprint import pprint

d = difflib.Differ()


f1 = open("students.csv")
c1 = f1.readlines()
f1.close()

f2 = open("students_updated.csv")
c2 = f2.readlines()
f2.close()

result = d.compare(c1, c2)

pprint(list(result))

