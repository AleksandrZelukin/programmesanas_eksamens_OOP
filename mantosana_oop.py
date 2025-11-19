class Transport_lidzeklis:
    def tr(self):
        pass
    
class Automobilis(Transport_lidzeklis):
    def __init__(self,modelis, gads):
        self.modelis = modelis
        self.gads = gads
    def tr(self):
        return f"Automobilis: {self.modelis}, Gads: {self.gads}"
        # return  ("Automobilis:",self.modelis, "Gads:", self.gads)
    
class Motocikls(Transport_lidzeklis):
    def __init__(self,modelis, gads):
        self.modelis = modelis
        self.gads = gads
    def tr(self):
        return f"Motocikls: {self.modelis}, Gads: {self.gads}"
    
auto1 = Automobilis("Toyota", 2020)
moto1 = Motocikls("Yamaha", 2019)   
print(auto1.tr())
print(moto1.tr())