import mysql.connector as m
con = m.connect(host="localhost", password="",
                user="root", database="mydatabse")
mycursor = con.cursor()
mycursor = con.execute("delete from employee where department='Computer'")
print("Computer Department Delete Sucessfully")
con.commit()
rc = mycursor.rowcount
print("Total Number of Row Affected:", rc)
con.close()
