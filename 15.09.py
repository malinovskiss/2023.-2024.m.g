import PySimpleGUI as psg

#minimalas prasības
class info():
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def apskate(self):
        print(self.modelis)
        print(self.cena)
        print(self.veids)

    def labosana(self, veids, modelis,cena,):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena
        with open('info.txt',encoding="utf=8") as file:
            lines = file.readline()
    
    
    
    def save(self):
        with open('info.txt','a', encoding="utf=8") as fails:
            fails.write("-Personālā datora sastāvdaļa-\n")
            fails.write(f"Veids: {self.veids}\n")
            fails.write(f"modelis: {self.modelis}\n")
            fails.write(f"Cena: {self.cena} EUR\n")


psg.theme('darkamber')
layout = [
            [psg.Text('Komponentes')],
            [psg.Text('Veids'),psg.InputText()],    
            [psg.Text('Modelis'),psg.InputText()],
            [psg.Text('Cena'),psg.InputText()],
            [psg.Button('Saglabāt')]
            
          ]

layout2 = [
            [psg.Text('Redigēšana')], 
            [psg.Text('Veids'),psg.InputText()],    
            [psg.Text('Modelis'),psg.InputText()],
            [psg.Text('Cena'),psg.InputText()],
            [psg.Button('Saglabāt')]
        
        ]

loguGrupa = [[
    psg.TabGroup(
        [
            [
                psg.Tab('Datu ievade', layout),
                psg.Tab('Datu redigēšana', layout2)
            
            ]
        ]
    ),
    psg.Button('Aizvērt')
    
    
]]

window = psg.Window('Datora komponentes', loguGrupa)
#Pārbauda notikumus grafiskajā saskarnē
while True:
    event,values = window.read() 
    #Nolasa ievadītās vērtības un darbības
    #Apgalvojumi
    if event == "Saglabāt":
        print(values)
        veids = values[0]
        modelis = values[1]
        cena = values [2]
        jauns = info(veids,modelis,cena)
        jauns.apskate()

    if event == "Rediģēšana":
        print(values)
        veids = values[3]
        modelis = values[4]
        cena = values [5]
        jauns = info(veids,modelis,cena)
        jauns.apskate()
    
    if event in (psg.WIN_CLOSED,'Aizvērt'):
        break

window.close()