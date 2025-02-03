class Piemers:
    def __init__(self,color,form):
        self.color = color
        self.form = form
        
obj1 = Piemers("red","circle")
obj2 = Piemers("blue","triangle")

print(obj1.color,obj1.form)
print(obj2.color,obj2.form)