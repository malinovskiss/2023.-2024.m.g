import PySimpleGUI as psg

class Noma():

    def __init__(self, Produkta_kategorija, Produkta_nosaukums, Tehniskie_raksturojumi, Nomas_cena_diena, Produkts_pieejams, Nomnieks_vards, Nomnieks_uzvards, Nomnieks_pk,Nomnieks_tel_numurs, Nomas_sakuma_datums, Nomas_beigu_datums):
        self.Produkta_kategorija = Produkta_kategorija
        self.Produkta_nosaukums = Produkta_nosaukums
        self.Tehniskie_raksturojumi = Tehniskie_raksturojumi
        self.Nomas_cena_diena = Nomas_cena_diena
        self.Produkts_pieejams = Produkts_pieejams
        self.Nomnieks_vards = Nomnieks_vards
        self.Nomnieks_uzvards = Nomnieks_uzvards
        self.Nomnieks_pk = Nomnieks_pk
        self.Nomnieks_tel_numurs = Nomnieks_tel_numurs
        self.Nomas_sakuma_datums = Nomas_sakuma_datums
        self.Nomas_beigu_datums = Nomas_beigu_datums
    def produktu_info(self):
        pass
    
    def save(self):
        with open('info.txt','w', encoding="utf=8") as fails:
            fails.write('Noma')
            fails.write(self.Produkta_kategorija)
            fails.write(self.Produkta_nosaukums)
            fails.write(self.Tehniskie_raksturojumi)
            fails.write(self.Nomas_cena_diena)
            fails.write(self.Produkts_pieejams)
            fails.write(self.Nomnieks_vards)
            fails.write(self.Nomnieks_uzvards)
            fails.write(self.Nomnieks_pk)
            fails.write(self.Nomnieks_tel_numurs)
            fails.write(self.Nomas_sakuma_datums)
            fails.write(self.Nomas_beigu_datums)
psg.theme('LightGreen4')

layout = [ 
        [psg.Text('Ievadiet produkta informāciju')],
        [psg.Text('Produkta kategorija'),psg.InputText()],
        [psg.Text('Produkta nosaukums'),psg.InputText()],
        [psg.Text('Produkta raksturojums'),psg.InputText()],
        [psg.Text('Nomas cena dienā (EUR)'),psg.InputText()],
        [psg.Text('Vai šis produkts ir pieejams?')],
        [psg.Radio('Jā', "a", default=True),psg.Radio('Nē', "a", default=False)]
]

layout2 = [
    [psg.Text('Ievadīt nomnieka informāciju')],
    [psg.Text('Vārds:'),psg.InputText()],
    [psg.Text('Uzvārds:'),psg.InputText()],
    [psg.Text('Personas kods:'),psg.InputText()],
    [psg.Text('Telefona numurs:'),psg.InputText()],
    [psg.Text('Nomas sākuma datums:'),psg.InputText()],
    [psg.Text('Nomas beigu datums:'),psg.InputText()],

]

Tabgroup = [
    [
    psg.TabGroup(
        [   
            [
            psg.Tab('Produkta_info', layout),
            psg.Tab('Nomnieka_info', layout2)
                
            ]
            
        ]
        
    )],
    [psg.Button('Saglabāt informāciju'),psg.Button('Atcelt')]
]
window =psg.Window('Noma', Tabgroup)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel': 
        break 
    print(values[0])
    
if event in (psg,'labi'):
        save = Noma(values[0],values[2],values[3],values[4],values[5])
        save.save()

window.close() 
