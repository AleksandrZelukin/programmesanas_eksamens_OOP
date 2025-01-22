# https://www.w3schools.com/python/python_classes.asp

class Skolens:
    def __init__(self,vadrs,uzvards,klase):
        self.vards = vadrs
        self.uzvards = uzvards
        self.klase = klase
    def grupa(self):
        print("Sveiks, es esmu" , self.vards , self.uzvards , self.klase)    
        
sk1 = Skolens("Jana","Liepa","10.a")

sk2 = Skolens("Eva","Ozola","12.c")

print(sk1.klase) # The __init__() Function
sk2.grupa() # Object Methods