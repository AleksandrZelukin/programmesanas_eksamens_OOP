class Product():
    def __init__(self,name,price,daudzums):
        self.name = name
        self.price = price
        self.daudzums = daudzums
    def get_total_price(self):
        total_price = self.price*self.daudzums
        return total_price
    
class PirkumuGrozs():
    def pievienot_grozam(self,product):
        print("Produkts",product.name,"pievienots grozam!")
    def izdests_no_grozam(self,product):
        print("Produkts",product.name,"nodzēsts no groza!")
    def get_total_price(self,product):
        print("Kopējā simma",product.get_total_price()) 
        

Olas = Product("Balticovo",0.17,12)
Maize = Product("Rupjmaize",2.40,2)
print(Olas.get_total_price())
print(Maize.get_total_price())

Pirkumi = PirkumuGrozs()
Pirkumi.pievienot_grozam(Olas)
Pirkumi.pievienot_grozam(Maize)
Pirkumi.get_total_price(Olas)
Pirkumi.get_total_price(Maize)
Pirkumi.izdests_no_grozam(Olas)
