import PySimpleGUI as psg

class noma():
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

psg.theme('darkamber')
layout = [
    [psg.Text('a')]
]

window = psg.Window('Produkts_pieejams', layout)

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
                psg.Tab('Produkta info', layout),
                psg.Tab('Nomnieka info', layout2)
            
            ]
        ]
    ),
[psg.Button('Aizvērt'),
    psg.Button('Datu apskate')]

]]

window.close() 
