# Pirma daļa https://youtu.be/9sf6yGguEl8?si=dCNhRa6sQGeLPipV
# Otra daļa https://youtu.be/l1ig2dkdpsY?si=nnDKN_Og--jfBs4_
class Product():
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        total_price = self.price*self.quantity
        return total_price

class ShoppngCart():
    def add_product_to_cart(self,product):
        print("Produkts",product.name,"pievienots grozam!")
    def remove_product_from_cart(self,product):
        print("Produkts",product.name,"nodzēsts no groza!")
    def get_total_price(self,product):
        print("Kopējā simma",product.get_total_price())    

class SystemUser():
    def __init__(self,usename,password,email):
        self.username = usename
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
        print("E-pasts:",self.email)
            
Maize = Product("Baltmaize",1.50,2)
print("Kopējā cena par maizi: ",Maize.get_total_price())
Desina = Product("Doktordesa", 3.50,2)
print("Kopējā cena par desiņu: ",Desina.get_total_price())

IepirkumuGrozs = ShoppngCart()
IepirkumuGrozs.add_product_to_cart(Maize)
IepirkumuGrozs.get_total_price(Maize)
IepirkumuGrozs.remove_product_from_cart(Maize)

Vasya = SystemUser("Vasilijs","qwerty","va@mail.com")
Vasya.set_user_info("Vasilijs","123456","va@mail.com")
Vasya.get_user_info()
