class Product():
    def __init__(self,name,price,daudzums):
        self.name = name
        self.price = price
        self.daudzums = daudzums

    def get_total_price(self):
        total_price = self.price*self.daudzums
        return total_price

class IepirkumuGrozs():
    def add_product_to_cart(self,product):
        print("Produkts",product.name,"Pievienots grozam!")
    def remove_product_from_cart(self,product):
        print("Produkts",product.name,"nodzēsts no groza!")
    def get_total_price(self,product):
        total_price = product.get_total_price()
        print("Kopējē summa:",total_price)


Olas = Product("Olas",0.20,10)
Piens = Product("Piens",1.15,2)
Desa = Product("Desa",3.50,1)
Siers = Product("Siers",2.50,1)

# print("Olas kopējā cena:",Olas.get_total_price())
# print("Piens kopējā cena:",Piens.get_total_price())

Grozs = IepirkumuGrozs()
Grozs.add_product_to_cart(Olas)
Grozs.add_product_to_cart(Piens)
Grozs.add_product_to_cart(Desa)
Grozs.add_product_to_cart(Siers)

Grozs.get_total_price(Olas)
Grozs.get_total_price(Piens)
Grozs.get_total_price(Desa)
Grozs.get_total_price(Siers)


class IepirkumuGrozs():
    def __init__(self):
        self.products = []
    def add_product_to_cart(self, product):
        self.products.append(product)
        print("Produkts", product.name, "Pievienots grozam!")
    def get_total_price(self, product=None):
        total_price = 0
        if product:
            total_price = product.get_total_price()
        else:
            total_price = sum(p.get_total_price() for p in self.products)
        print("Kopējā summa:", total_price)




Grozs = IepirkumuGrozs()
Grozs.add_product_to_cart(Olas)
Grozs.add_product_to_cart(Piens)
Grozs.add_product_to_cart(Desa)
Grozs.add_product_to_cart(Siers)

Grozs.get_total_price(Olas)
Grozs.get_total_price(Piens)
Grozs.get_total_price(Desa)
Grozs.get_total_price(Siers)

# Вывод полной стоимости всех продуктов
Grozs.get_total_price()
