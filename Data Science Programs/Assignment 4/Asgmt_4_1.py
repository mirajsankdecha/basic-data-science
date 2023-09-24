import mysql.connector as m
con = m.connect(host="localhost", user="root", password="")
c1 = con.cursor()
c1.execute("create database mydatabase")
print("Data Base Connect Sucessfully")
print(con)
con.commit()
con.close()
