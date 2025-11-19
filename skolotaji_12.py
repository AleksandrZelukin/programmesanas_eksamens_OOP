class Skolotajs:
    def __init__(self,vards, uzvards,stundas):
        self.vards = vards
        self.uzvards = uzvards
        self.stundas = stundas
        self.skol_tips = 0       
    def info(self):
        return f"Skolotājs: {self.uzvards}, stundas nedeļā: {self.stundas}"

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, vards, uzvards, stundas, klase):
        super().__init__(vards, uzvards, stundas)
        self.klase = klase
        self.skol_tips = 1
    def info(self):
        return f"Sākumskolas skolotājs klasei: {self.klase}"


class PamatskolasSkolotajs(Skolotajs):
    def __init__(self, vards, uzvards, stundas, specialitate):
        super().__init__(vards, uzvards, stundas)
        self.specialitate = specialitate
        self.skol_tips = 2
    def info(self):
        return f"Pamatskolas skolotājs specialitāte: {self.specialitate}"
   
skolotajs1 = SakumskolasSkolotajs("Jānis", "Bērziņš", 20, "3.A")
skolotajs2 = PamatskolasSkolotajs("Anna", "Kalniņa", 18, "Matemātika")

print(skolotajs1.uzvards, skolotajs1.stundas, skolotajs1.klase) 
print(skolotajs2.uzvards, skolotajs2.stundas, skolotajs2.specialitate)