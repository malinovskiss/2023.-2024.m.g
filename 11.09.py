import csv

class sastavdalas():
    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
    
    def izdrukat(self):
        print("Veids: ", self.veids)
        print("Modelis: ", self.modelis)
        print("Cena: ", self.cena)

    def saglabat(self):
        with open('sastavdala.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerow(['Veids','Modelis','Cena'])
            csvwrite.writerow([self.veids, self.modelis, self.cena])
dators = sastavdalas(veids='RAM',modelis= 'Corsair Vengeance LPX 16GB',cena= '99,99 EUR')
print(dators.veids)
