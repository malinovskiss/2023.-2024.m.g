#Minimālās prasības
class sastavdalas():
    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    
    def apskate(self):
        print(self.modelis)

    def labosana(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

jauns = sastavdalas("RAM","Corsair Vengeance LPX 16GB",99.99)
jauns.apskate()
jauns.labosana("GPU","GeForce",75.5)
jauns.apskate()
#Datu saglabāšana
