filename = input("Enter the File Name: ")
f = open(filename, "w")
data = input("Enter the Data: ")
f.write(data)
f.close()