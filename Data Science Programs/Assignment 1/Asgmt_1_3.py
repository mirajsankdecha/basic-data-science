class Drawing:
    def getdata(self):
        self.length=float(input("Enter the Length:"))
        self.width=float(input("Enter the Width:"))
    def putdata(self):
        print(self.length,self.width)
        
class Rect(Drawing):
    pass
    
obj=Rect()
obj.getdata()
obj.putdata()
    
