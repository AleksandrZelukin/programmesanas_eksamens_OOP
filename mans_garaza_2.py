class Automobili:
    def __init__(self, marka, modelis, gads, nobraukums):
        self.marka = marka
        self.modelis = modelis
        self.gads = gads
        self.nobraukums = nobraukums

    def apraksts(self):
        return f"{self.gads} {self.nobraukums} {self.marka} {self.modelis}"

    def nomainit_nobraukumu(self, jauns_nobraukums):
        self.nobraukums = jauns_nobraukums
        print(f"Nobraukums nomainīts uz {self.nobraukums}")

auto1 = Automobili("Toyota", "Corolla", 2020, 15000)
print(auto1.apraksts())