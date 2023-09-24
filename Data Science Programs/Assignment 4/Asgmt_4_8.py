import mysql.connector as m

con = m.connect(host="localhost", password="",
                user="root", database="mydatabase")
mycursor = con.cursor()
mycursor.execute("drop table employee;")
print("Table Drop Sucessfully")
con.commit()
con.close()
