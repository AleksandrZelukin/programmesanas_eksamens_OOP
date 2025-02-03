class Transports:
    def go (self):
        pass

class Car(Transports):
    def go (self):
        print("Your drive the car")

class Motorcycle(Transports):
    def go (self):
        print("You ride the motorcycle")

        
transports = Transports()
car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.go()
