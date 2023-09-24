import mysql.connector as m

con = m.connect(host="localhost", password="",
                user="root", database="mydatabase")
mycursor = con.cursor()
mycursor = con.execute(
    "alter table employee add column Dateofjoin(varchar(15));")
print("One Column Added!")
mycursor.commit()
con.close()
