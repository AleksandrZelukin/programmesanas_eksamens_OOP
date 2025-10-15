class Product():
    def __init__(self,name,price,daudzums):
        self._name = name
        self._price = price
        self._daudzums = daudzums

    def get_total_price(self):
        total_price = self._price * self._daudzums
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
        print("Produkts", product._name, "Pievienots grozam!")
    def remove_product_from_cart(self, product):
        self.products.remove(product)
        print("Produkts", product._name, "Nodzēsts no groza!")
    def get_total_price(self,product=None):
        total_price = sum(products._price * products._daudzums for products in self.products)
        # print("Kopējā summa:", total_price)

Grozs = IepirkumuGrozs()
Grozs.add_product_to_cart(Olas)
Grozs.add_product_to_cart(Piens)
Grozs.add_product_to_cart(Desa)
Grozs.add_product_to_cart(Siers)

Grozs.remove_product_from_cart(Desa)

# 'pilnu groza' cenu aprēķins
# Grozs.get_total_price()

class Lietotajs():
    def __init__(self,vards,parole,epasts):
        self.vards = vards
        self.parole = parole
        self.epasts = epasts
    def set_user_info(self,vards,parole,epasts):
        self.vards = vards
        self.parole = parole
        self.epasts = epasts
    def get_user_info(self):
        print("Lietotāja vārds:", self.vards)
        print("Lietotāja parole:", self.parole)
        print("Lietotāja epasts:", self.epasts)

class Pircejs(Lietotajs):
    def __init__(self,vards,parole,epasts,customer_id,pirkumu_vesture,dalibnieka_statuss):
        super().__init__(vards,parole,epasts)
        self.customer_id = customer_id
        self.pirkumu_vesture = pirkumu_vesture
        self.dalibnieka_statuss = dalibnieka_statuss
    def get_user_info(self):
        print("Pircēja vārds:", self.vards)
        print("Pircēja parole:", self.parole)
        print("Pircēja epasts:", self.epasts)
        print("Pircēja ID:", self.customer_id)
        print("Pirkumu vēsture:", self.pirkumu_vesture)
        print("Dalībnieka statuss:", self.dalibnieka_statuss)
    def set_user_info(self,vards,parole,epasts,customer_id,pirkumu_vesture,dalibnieka_statuss):
        super().set_user_info(vards,parole,epasts)
        self.customer_id = customer_id
        self.pirkumu_vesture = pirkumu_vesture
        self.dalibnieka_statuss = dalibnieka_statuss
    def add_purchase_history(self,purchase):
        self.pirkumu_vesture.append(purchase)
        print("Pirkums", purchase, "pievienots pirkumu vēsturei!")



Pircejs1 = Pircejs("Juris","parole789","juris@example.com",1,[],"aktīvs")
Pircejs1.get_user_info()
# Pircejs1.set_user_info("Marta","parole321","velta@example.com",2,[],"neaktīvs")
# Pircejs1.get_user_info()
Pircejs1.add_purchase_history("Olas, Piens")

Pircejs1.get_user_info()
Grozs.get_total_price()
print("Pircēja pirkumu vēsture:", Pircejs1.pirkumu_vesture)
print("Pircēja dalībnieka statuss:", Pircejs1.dalibnieka_statuss)

