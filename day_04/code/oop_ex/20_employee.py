class employee:


    # Data/attributes
    def __init__(self, empname, empage, empcompany):
        print('SELF:', self)
        self.name    = empname
        self.age     = empage
        self.salary  = ''
        self.company = empcompany
        self.country = ''
        self.tax     = 0


    # Member functions/methods

    def printstatus(self):
        print(self.name, self.age, self.salary, self.company, self.country)
        print('TAX:', self.tax)

    # setter
    def setsalary(self, empsal):
        self.salary = empsal

    # getter
    def getsalary(self):
        return self.salary

    # logic
    def calctax(self):
        self.tax = 0.1 * float(self.salary)

    def gettax(self):
        return self.tax
# -------------------------------------------------------------------------


e1 = employee('Anil', 30, 'oracle')
e2 = employee('Sunil', 21, 'genpact')

# -------------------------------------------------------------------------


e1.printstatus()
e2.printstatus()

#e1.salary = '1000000'
e1.setsalary('1000000')
e2.setsalary('2000000')

e1.printstatus()
e2.printstatus()

print('E1 :', e1.getsalary())
print('E2 :', e2.getsalary())

e1.calctax()
e2.calctax()

e1.printstatus()
e2.printstatus()

e1.xyz()
