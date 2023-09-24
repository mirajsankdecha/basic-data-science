import mysql.connector as m
con = m.connect(host="localhost", password="",
                user="root", database="mydatabase")
mycursor = con.cursor()
mycursor.execute("select * from employee;")
records = mycursor.fetchall()
for record in records:
    print(record)
con.commit()
con.close()
