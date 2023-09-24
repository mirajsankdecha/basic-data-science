class GrandM:
    def getGM(self):
        self.height=float(input("Enter the Height of Grandmother:"))
        self.color=input("Enter the Color of Grandmother:")
    def dispGM(self):
        print(self.height)
        print(self.color)
        
class Mother(GrandM):
    def getM(self):    
        self.eyecolor=input("Enter the Eye Color of Mother:")
    def dispM(self):
        print(self.eyecolor)

class Daughter(Mother):
    pass

obj1=Daughter()
obj1.getGM()
obj1.dispGM()
obj1.getM()
obj1.dispM() 
        
