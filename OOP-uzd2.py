# https://youtu.be/l1ig2dkdpsY?si=yISmc3k1fJ3n0uO_
class Product():
    def __init__(self, name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    def get_total_price(self):
        total_price = self.__price*self.__quantity
        return total_price
    def get_product_name(self):
        return self.__name
    
class ShopingCart():
    def __init__(self):
        self.items = []
    def add_product_to_cart(self,product):
        print("Produkts",product.get_product_name(),"Pievienots grozam!")
        self.items.append(product)
    def remove_product_from_cart(self,product):
        print("Produkts",product.get_product_name(),"nodzēsts no groza!")
        self.items.remove(product)
    def get_total_price(self,product):
        total_price = 0
        for item in self.items:
            total_price += product.get_total_price()
        print("Kopējē summa:",total_price)
        
class SystemUser():
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    def set_user_info(self,newusername,newpassword,newemail):
        self.username = newusername
        self.password = newpassword
        self.email = newemail
        print("Informācija ir nomainīta!")
    def get_user_info(self):
        print("---Informācija par lietotāju---")
        print("Lietotājavārds:",self.username)
        print("Parole:",self.password)
        print("E-mail:",self.email)

class Customer(SystemUser):
    def __init__(self, username, password, email,customer_id,purchase_history,membership):
        super().__init__(username, password, email)
        self.customer_id = customer_id
        self.purshase_history = purchase_history
        self.membership = membership
    def set_user_info(self, newusername, newpassword, newemail,newcustomer_id,newpurchase_history,newmembership):
        super().set_user_info(newusername, newpassword, newemail)
        self.customer_id = newcustomer_id
        self.purshase_history = newpurchase_history
        self.membership = newmembership
    def get_user_info(self):
        super().get_user_info()
        print("Klienta ID:",self.customer_id)
        print("Pirkumu vēsture:",self.purshase_history)
        print("Piederiba programmām:",self.membership)


Maize = Product("Baltmaize", 1.50,2)
print("Kopējā cena par maizi:",Maize.get_total_price())
Desina = Product("Dokotrdesa",3.50,2)
print("Kopējā cena par desiņu:",Desina.get_total_price())


IepirkumuGrozs = ShopingCart()
IepirkumuGrozs.add_product_to_cart(Maize)
IepirkumuGrozs.get_total_price(Maize)
IepirkumuGrozs.remove_product_from_cart(Maize)

Vasija = SystemUser("Vasilijs","123","a@mail.com")
Vasija.set_user_info("Vasilijs","34567","a@mail.com")
Vasija.get_user_info()


Annina = Customer("Anna123", "qwerty","a@maio.com",13,"","")
Annina.set_user_info("Anna123", "qwerty","a@maio.com",13,"Vizbulītes","")
Annina.get_user_info()