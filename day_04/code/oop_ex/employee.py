class Employee:

    # Class variables
    empCount = 0

    # Constructor and Data Intialization
    def __init__(self, n, company, salary):
        self.name = n
        self.company = company
        self.salary = salary
        self.tax = 0
        self.a = 0
        self.max = 5
        Employee.empCount += 1


    # Functions

    # Python Compatibility Functions

    def __repr__(self):
        return self.name + ' ' + self.company + ' ' + self.salary
    
    def __str__(self):
        return self.name + ' ' + self.company + ' ' + self.salary

    def __len__(self):
        return Employee.empCount

    def __iter__(self):
        self.a = 0
        self.forloopinfo = [self.name, self.company, self.salary, self.tax, Employee.empCount]
        self.max = len(self.forloopinfo)
        return self

    def __next__(self):
        if self.a < self.max:
            x = self.forloopinfo[self.a]
            self.a += 1
            return x
        else:
            self.a = 0
            raise StopIteration


    def printinfo(self):
        print(self.name.upper())
        print('-'*30)
        print('COMPANY    :', self.company)
        print('SALARY     :', self.salary)
        print('TAX        :', self.tax)
        print('\n\n')

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])


'''

C:\Users\Purushotham\Desktop\oracle_aug\day_04\code\oop_ex>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from employee import Employee
>>> e = Employee('anil', 'oracle', '1000000 USD')
>>> for info in e:
...     print(info)
... 
anil
oracle
1000000 USD
0
1
>>> e
anil oracle 1000000 USD
>>> e
anil oracle 1000000 USD
>>> print(e)
anil oracle 1000000 USD
>>> len(e)
1
>>> for info in e:
...     print(info)
...
anil
oracle
1000000 USD
0
1
>>>

'''