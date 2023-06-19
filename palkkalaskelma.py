class PayrollSystem:
    def calculate_payroll(self, employees):
        
        for employee in employees:
            print("Palkkalaskelma")
            print("==============")
            salary = employee.calculate_salary()
            print("Henkilölle:", employee.id, "-", employee.name)
            print("- Maksetaan:", salary)
            print()

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

employees = []
id_counter = 1

while True:
    name = input("Anna työntekijän nimi: (0 lopetus): ")
    if name == '0':
        break

    monthly_salary = int(input("Anna kuukausipalkka: "))
    employee = SalaryEmployee(id_counter, name, monthly_salary)
    employees.append(employee)
    id_counter += 1

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
