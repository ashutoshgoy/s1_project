class Company:
    def __init__(self,name,project):
        self.name_of_company=name
        self._project_name=project

    def print_details(self):
        print(f"Name of the company={self.name_of_company}")
        print(f"Name of project={self._project_name}")
class Employee(Company):
    def __init__(self,eName,salary,company_name,project_name):
        Company.__init__(self,company_name,project_name)
        self.employee_name=eName
        self.employee_salary=salary

    def print_salary_details(self):
        print(f"salary of {self.employee_name} is {self.employee_salary}")
company=Company("Sigmoid","Abc bank")
print(company.name_of_company)
print(company._project_name)

employee=Employee("Ashutosh ","16500",company.name_of_company,company._project_name)
print(f"Hello {employee.employee_name},welcome to {employee.name_of_company}. You will be working in {employee._project_name}")
employee.print_details()
employee.print_salary_details()

