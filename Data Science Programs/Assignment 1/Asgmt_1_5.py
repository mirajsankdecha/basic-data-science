class Human:
    def input_Human(self):
        self.firstname=input("Enter the the Firstname:")
        self.lastname=input("Enter the Lastname:")
        self.gender=input("Enter the Gender:")
    def display_Human(self):
        print(self.firstname)
        print(self.lastname)
        print(self.gender)
class Employee(Human):
    def input_emp(self):
        self.company=input("Enter the Name of Company:")
        self.level=int(input("Enter the Level of Company:"))
    def display_emp(self):
        print(self.company)
        print(self.level)
obj=Employee()
obj.input_Human()
obj.input_emp()
obj.display_Human()
obj.display_emp() 

