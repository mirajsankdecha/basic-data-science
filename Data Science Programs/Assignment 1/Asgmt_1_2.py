class Employee:
    def getEmployee(self):
        self.emp_id=input("Enter the Id of Employee:")
        self.name=input("Enter the Name of Employee:")
        self.salary=float(input("Enter the Salary of Employee:"))
        self.date_of_join=input("Enter the date of join of Employee:")
    def showEmployee(self):
        print(self.emp_id)
        print(self.name)
        print(self.salary)
        print(self.date_of_join)
call=Employee()
call.getEmployee()
call.showEmployee()
        
        
