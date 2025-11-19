class Animal:
    def __init__(self, name):
        self.name = name
        
class Dogs(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    
my_dog = Dogs("Šariks","Labrador")
print(my_dog.name, my_dog.type)