import os
a = int(input("Enter the Value of A:"))
b = int(input("Enter the Value of B:"))
c = int(input("Enter the Value of C:"))
if(a < b and a < c):
    print("Min is A")
elif(b < a and b < c):
    print("Min is B")
elif(c < a and c < b):
    print("Min is C")
elif(a == b and a < c and b < c):
    print("Min is A and B")
elif(a == c and a < b and c < b):
    print("Min is A and C")
elif(b == c and b < a and c < a):
    print("Min is B and C")
elif(a == b and b == c and a == c):
    print("Min is All")
