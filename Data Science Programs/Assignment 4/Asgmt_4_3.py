import mysql.connector as m

con = m.connect(host="localhost", password="",
                user="root", database="mydatabase")
print(con)
mycursor = con.cursor()
for i in range(0, 5):
    emp_id = int(input("Enter Employee ID:"))
    emp_name = input("Enter the Employee Name:")
    city = input("Enter the Employee City:")
    salary = input("Enter the Salary of Employee:")
    department = ("Enter the Department of Employee:")
    designation = input("Enter the Designation of Employee:")
i = mycursor.execute("Insert into employee values({},'{}','{}',{},'{}','{}');".format(
    emp_id, emp_name, city, salary, department, designation))
print("Records Insert Sucessfully")
con.commit()
con.close()
