import re

i = input("Enter Your Password:")

a = 0
while True:
    if (len(i) <= 8 or len(i) >= 22):
        a = -1
        break
    elif not re.findall("[A-Z]", i):
        a = -1
        break
    elif not re.findall("[a-z]", i):
        a = -1
        break
    elif not re.findall("[\W]", i):
        a = -1
        break
    elif re.search("\s", i):
        a = -1
        break
    else:
        a = 0
        print("Valid Password")
        break

if a == -1:
    print("Not a Valid Password ")
