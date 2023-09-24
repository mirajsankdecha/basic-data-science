def rev():
    sum=0
    x=int(input("Enter the Number:"))
    while x>0:
            n=x%10
            sum=sum+n
           # print(n,end=" ")
            x=int(x/10)
    print("Total Sum is:",sum)
rev()             
