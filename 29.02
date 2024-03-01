import random

class VārduApguvesProgramma:
    def __init__(self):
        self.vārdnīca = {}

    def pievienot_vārdu(self, vārds, nozīme):
        self.vārdnīca[vārds] = nozīme

    def izveidot_testu(self):
        tests = []
        for vārds, nozīme in self.vārdnīca.items():
            tests.append((vārds, nozīme))

        random.shuffle(tests)
        return tests

    def izpildīt_testu(self, tests):
        rezultāts = 0
        kopējais_jautājumu_skaits = len(tests)

        for vārds, nozīme in tests:
            lietotāja_atbilde = input(f"Kas nozīmē vārdu '{vārds}'? ")
            if lietotāja_atbilde.lower() == nozīme.lower():
                print(" Pareizi!")
                rezultāts += 1
            else:
                print(f" Nepareizi! Pareizā atbilde ir '{nozīme}'.")

        print(f"\nJūsu rezultāts: {rezultāts}/{kopējais_jautājumu_skaits}")

# Piemēra izmantošana
apgūtājs = VārduApguvesProgramma()

# Pievienot vārdus vārdnīcai
apgūtājs.pievienot_vārdu("ābols", "auglis")
apgūtājs.pievienot_vārdu("grāmata", "rakstīts vai drukāts darbs, kas sastāv no lappusēm, kas ir salīmētas vai šūtas kopā gar vienu malu")

# Izveidot testu
tests = apgūtājs.izveidot_testu()

# Izpildīt testu
apgūtājs.izpildīt_testu(tests)
