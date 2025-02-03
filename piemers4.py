class Piemers:
    color = "red"
    form = "circle"
    def changecolor (self,color1):
        self.color = color1
    def changeform (self,newform):
        self.form = newform
        
obj1 = Piemers()
obj2 = Piemers()
obj3 = Piemers()   
print(obj1.color, obj1.form) 

obj1.changecolor("blue")
obj1.changeform("triangle")  
obj2.changecolor("yellow")
obj3.changecolor("orange")

print(obj1.color, obj1.form) 
print(obj2.color, obj1.form) 
print(obj3.color, obj3.form) 