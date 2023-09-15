#minimālās prasības
class datora_sastavdala():
    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    
    def izdrukat(self):
        print("Veids: ", self.veids)
        print("Modelis: ", self.modelis)
        print("Cena: ", self.cena)
    
    def labosana(self,veids,modelis,cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def saglabat(self):
        
        with open('sastavdalas.txt', 'w', encoding="utf-8") as fails :
            fails.write("-datora sastāvdaļas-")
            fails.write(" \n")
            fails.write(str(dators.veids))
            fails.write(" \n")
            fails.write(str(dators.modelis))
            fails.write(" \n")
            fails.write(str(dators.cena))

dators = datora_sastavdala(veids='RAM',modelis= 'Corsair Vengeance LPX 16GB',cena= '99,99 EUR')
dators.izdrukat()


#datu saglabāšana

dators.saglabat()

import PySimpleGUI as psg

psg.theme('DarkAmber')
logs = [
        [psg.Text('Komponents')],
        [psg.Text('Veids'),psg.InputText()],
        [psg.Text('Modelis'),psg.InputText()],
        [psg.Text('Cena'),psg.InputText()],
        [psg.Button('Saglabāt')]
]
logs2 = [
    [psg.Text("Rediģēšana")],
    [psg.Text('Veids'),psg.InputText()],
    [psg.Text('Modelis'),psg.InputText()],
    [psg.Text('Cena'),psg.InputText()],
    [psg.Button('Rediģēt')]    
    
]

logugrupa = [[
    psg.TabGroup(
        [
         [
            psg.Tab('Datu ievade',logs),
            psg.Tab('Datu rediģēšana',logs2)
         ]   
        ]
    ),
    psg.Button('Aizvērt')
]]
window = psg.Window('Datora komponentes', logugrupa)

while True:
    event,values = window.read()
    
    if event == "Saglabāt":
        veids =  values[0]
        modelis = values[1]
        cena = values[2]
        dators = datora_sastavdala(veids,modelis,cena)
        dators.saglabat()
        
    if event == "Rediģēt":
        veids = values[3]
        modelis = values[4]
        cena = values[5]
        dators.labosana(veids,modelis,cena)
        dators.saglabat()

if event == "Datu apskate":
        psg.theme("BlueMono")
        layout = [
                  [psg.Text("Esošās komponentes")],
                  [psg.Text("Veids: " + values[0])],
                  [psg.Text(
    
    if event in (psg.WIN_CLOSED, 'Aizvērt'):
        break
    

window.close()
