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
        print(f"veids ir {self.veids}, modelis ir{self.modelis}, krāsa - {self.cena}")

    def cenas_maina(self, jaunaCena):
        print(f"Iepriekšējā datora cena - {self.cena}")
        print(f"Jaunā datora cena - {jaunaCena}")

sastavdala = Dators(modelis="Corsair Vengeance",cena="99,99 EUR")

sastavdala.dati()
sastavdala.cenas_maina("100 EUR")