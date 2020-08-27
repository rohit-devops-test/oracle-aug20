# (CORE) DEVELOPER MINDSET

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
        print('\n\n')

    def setsalary(self, newsalary):
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self):
        self.tax = 0.1 * float(self.salary.split()[0])

# ------------------------------------------------------------------

# USER/APP DEVELOPER


# Infrastructure for three emploees are created

e1 = Employee('Anil', ' Oracle', "1000000 INR")
e2 = Employee('Sunil', ' Oracle', "1000000 INR")
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

