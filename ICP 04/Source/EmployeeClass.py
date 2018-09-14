class Employee:
    total_employee = 0
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    def getEmployeeInfo(self):
        print("The name of the employee is ",self.name)
        print("The family of the employee is ",self.family)
        print("The salary of the employee is ",self.salary)
        print("The department of the employee is ",self.department)
        print("\n")

    def average(self):
        empList = [employee1, employee2, employee3, employee4, employee5]
        for emp in empList:
            print(emp.salary)
        sum1 = sum([int(emp.salary) for emp in empList])
        avgSalary = sum1/len(empList)
        print("\n The average salary of all the employees is",avgSalary)

    def totalEmployeeCount(self):
        Employee.total_employee = Employee.total_employee+1

class FulltimeEmployee(Employee):
    def __init__(self,visa):
        super().__init__(name="Fatema",family="Hasta",salary="70,000",department="Software Dept")
        self.visa = visa

    def getFulltimeEmployeeInfo(self):
        print("The visa status of the employee is ",self.visa)


employee1 = Employee("Fatema","Hasta","70000","Software Dept")
print("***************************Employee 1****************************")
employee1.getEmployeeInfo()
employee1.totalEmployeeCount()

employee2 = Employee("Vinay","Jois","80000","HR Dept")
print("***************************Employee 2****************************")
employee2.getEmployeeInfo()
employee2.totalEmployeeCount()

employee3 = Employee("John","Abraham","60000","Software Dept")
print("***************************Employee 3****************************")
employee3.getEmployeeInfo()
employee3.totalEmployeeCount()

employee4 = Employee("Reshma","Jame","50000","HR Dept")
print("**************************Employee 4****************************")
employee4.getEmployeeInfo()
employee4.totalEmployeeCount()

employee5 = Employee("Sej","Morrow","90000","Software Dept")
print("***************************Employee 5****************************")
employee5.getEmployeeInfo()
employee5.totalEmployeeCount()


print("****************Total Employees are", Employee.total_employee)

femployee1 = FulltimeEmployee("H1B visa")
print("***************************Full time Employee****************************")
femployee1.getEmployeeInfo()
femployee1.getFulltimeEmployeeInfo()

employee1.average()

