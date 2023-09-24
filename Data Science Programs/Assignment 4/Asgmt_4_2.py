import mysql.connector as m
con = m.connect(host="localhost", user="root",
                password="", database="mydatabase")
print(con)
c1 = con.cursor()
c1.execute("create table employee(emp_id int(10),emp_name varchar(20),city varchar(15),salary int(10),department varchar(25),designation varchar(25));")
print("Employee Table Create Sucessfully")
con.commit()
con.close()
