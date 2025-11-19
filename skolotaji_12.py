class Skolotajs:
    def __init__(self,uzvards,stundas):
        self.uzvards = uzvards
        self.stundas = stundas
        
    def info(self):
        return f"Skolotājs: {self.uzvards}, stundas nedeļā: {self.stundas}"
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, stundas, klase):