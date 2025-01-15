class Product():
    def __init__(self,name,price,daudzums):
        self.name = name
        self.price = price
        self.daudzums = daudzums
    def get_total_price(self):
        total_price = self.price*self.daudzums
        return total_price


Olas = Product("Balticovo",0.17,12)
Maize = Product("Rupjmaize",2.40,2)
print(Olas.get_total_price())
print(Maize.get_total_price())
