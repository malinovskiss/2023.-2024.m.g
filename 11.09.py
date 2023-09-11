class Dators():
    def _init_(self,veids,modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

sastavdalas = Dators(veids = "RAM", modelis = "Corsair Vengeance", cena = "99,99 EUR")

print(sastavdalas.modelis)

class Dators():
    def _init_(self,veids,modelis,cena):
        self.modelis = cena
        self.cena = cena

    def dati(self):
        print(f"veids ir {self.veids}, modelis ir{self.modelis}, cena - {self.cena}")

