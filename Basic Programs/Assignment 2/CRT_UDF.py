def circle(r):
    return 3.14*r*r

r=int(input("Enter the Radius:"))
area=circle(r)
print("Area of Circle is:",area)

def rect(l,b):
    return l*b

l=int(input("Enter the Length:"))
b=int(input("Enter the Breath:"))
area=rect(l,b)
print("Area of Rectangle is:",area)

def tri(b,h):
    return 0.5*b*h

b=int(input("Enter the Breath for Triangle:"))
h=int(input("Enter the Height:"))
area=tri(b,h)
print("Area of Triangle is:",area)
