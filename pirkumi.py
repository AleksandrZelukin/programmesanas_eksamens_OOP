class Product():
    def __init__(self,name,price,daudzums):
        self.name = name
        self.price = price
        self.daudzums = daudzums

    def get_total_price(self):
        total_price = self.price*self.daudzums
        return total_price


Olas = Product("Olas",0.20,10)
Piens = Product("Piens",1.15,2)
Desa = Product("Desa",3.50,2)
Siers = Product("Siers",2.50,5)


class IepirkumuGrozs():
    def __init__(self,produkts=None):
        self.products = []
    def add_product_to_cart(self, product):
        self.products.append(product)
        print("Produkts", product.name, "Pievienots grozam!")
    def get_total_price(self,product=None):
        total_price = sum(products.price*products.daudzums for products in self.products)
        print("Kopējā summa:", total_price)



Grozs = IepirkumuGrozs()
Grozs.add_product_to_cart(Olas)
Grozs.add_product_to_cart(Piens)
Grozs.add_product_to_cart(Desa)
Grozs.add_product_to_cart(Siers)


# 'pilnu groza' cenu aprēķins
Grozs.get_total_price()
