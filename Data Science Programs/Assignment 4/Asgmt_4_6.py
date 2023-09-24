import mysql.connector as m
con = m.connect(host="localhost", password="",
                user="root", database="mydatabase")
mycursor = con.cursor()
mycursor.con.execute("update employee set salary=salary+(salary*5/100)")
print("Salary update Sucessfully")
con.commit()
con.close()
