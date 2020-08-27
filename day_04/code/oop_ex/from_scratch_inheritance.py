class Employee:

    # Class variables
    empCount = 0

    # Constructor and Data Intialization
    def __init__(self, n, company, salary):
        self.name = n
        self.company = company
        self.salary = salary
        self.tax = 0
        Employee.empCount += 1

    # Functions
    def printinfo(self):
        print(self.name.upper())
        print('-'*30)
        print('COMPANY    :', self.company)
        print('SALARY     :', self.salary)
        print('TAX        :', self.tax)
        

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])

#---------------------------------------------------------------

# CORE DEVELOPER -> Inheritance

class newemp(Employee):
    pass

class extEmployee(Employee):

    # Class variables
    # empCount is already available here

    # Constructor and Data Initialization
    # Supposed to distribute the data between parent and child
    def __init__(self, n, age, company, salary):
        super().__init__(n, company, salary)
        self.age = age
        self.addr = ''

    # Functions

    # All functions of Employee is also available here

    # Overridden function
    def printinfo(self):
        super().printinfo()
        print('-'*30)
        print('AGE        :', self.age)
        print('ADDRESS    :', self.addr)
        print('\n\n')

    # New functions
    def setaddr(self, addr):
        self.addr = addr


# --------------------------------------------------------------

# USER -> testing newemp


'''
# Infrastructure for three emploees are created

e1 = newemp('Anil', ' Oracle', "1000000 INR")
e2 = newemp('Sunil', ' Oracle', "1000000 INR")
e3 = Employee('Raj', ' Oracle', "1000000 INR")

# Now we can work with the infrastructure

emplist = [e1, e2, e3]
for obj in emplist:
    obj.printinfo()

print('Calculating taxes\n')

for obj in emplist:
    obj.calctax()

for obj in emplist:
    obj.printinfo()


# Give a hike of 15%
print('Calculating Hikes\n')

for obj in emplist:
    currsal = obj.getsalary()
    newsal = str(int(currsal.split()[0]) + 0.15 * int(currsal.split()[0])) + ' INR'
    obj.setsalary(newsal)

for obj in emplist:
    obj.printinfo()   

print('Employee Count: ', e1.empCount)

e4 = Employee('Rajesh', ' Oracle', "1000000 INR")

print('Employee Count: ', e3.empCount)

'''

# --------------------------------------------------------------

# USER -> Inheritance allows full backward compatibility with
#         Parent Class/Base Class

# Infrastructure for three emploees are created

e1 = extEmployee('Anil', 35, 'Oracle', "1000000 INR")
e2 = extEmployee('Sunil', 45, 'Oracle', "2000000 INR")
e3 = extEmployee('Raj', 55, 'Oracle', "3000000 INR")

# Now we can work with the infrastructure

emplist = [e1, e2, e3]
for obj in emplist:
    obj.printinfo()

e1.setaddr('J P Nagar, Bangalore')
e2.setaddr('Anna Nagar, Chennai')
e3.setaddr('Shivaji Nagar, Mumbai')

print('Calculating taxes\n')

for obj in emplist:
    obj.calctax()

for obj in emplist:
    obj.printinfo()


# Give a hike of 15%
print('Calculating Hikes\n')

for obj in emplist:
    currsal = obj.getsalary()
    newsal = str(int(currsal.split()[0]) + 0.15 * int(currsal.split()[0])) + ' INR'
    obj.setsalary(newsal)

for obj in emplist:
    obj.printinfo()   

print('Employee Count: ', e1.empCount)

e4 = Employee('Rajesh', ' Oracle', "1000000 INR")

print('Employee Count: ', e3.empCount)

# --------------------------------------------------------------

# USER -> Polymorphism

e1 = Employee('Anil', 'Oracle', "1000000 INR")
e2 = extEmployee('Anil', 35, 'Oracle', "1000000 INR")

obj = e2

obj.printinfo()