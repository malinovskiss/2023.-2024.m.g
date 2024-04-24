#1.uzd
import re

def validate_email(email):
    # Regulārā izteiksme, lai pārbaudītu e-pasta adreses formātu
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def register():
    while True:
        email = input("Ievadiet savu e-pasta adresi: ")
        if validate_email(email):
            break
        else:
            print("Nepareizs e-pasta formāts. Lūdzu, ievadiet e-pastu atkārtoti.")

    while True:
        password = input("Ievadiet paroli: ")
        if len(password) < 6:
            print("Parolei jābūt vismaz sešus simbolus garai. Lūdzu, ievadiet paroli atkārtoti.")
        else:
            print("Pateicamies par reģistrāciju!")
            break

register()

#2.uzd
import json

def nolasi_dzivniekus(fails):
    with open(fails, 'r', encoding='utf-8') as f:
        dzivnieki = json.load(f)
    return dzivnieki

def analize_dzivnieku_sugu(dzivnieki):
    sugas_skaits = {}
    for dzivnieks in dzivnieki:
        suga = dzivnieks['suga']
        if suga in sugas_skaits:
            sugas_skaits[suga] += 1
        else:
            sugas_skaits[suga] = 1
    
    print("Dzīvnieku sugas un to skaits:")
    for suga, skaits in sugas_skaits.items():
        print(f"{suga}: {skaits}")

def analize_dzivnieku_krasu(dzivnieki):
    krasu_skaits = {}
    for dzivnieks in dzivnieki:
        krasa = dzivnieks['kraasa']
        if krasa in krasu_skaits:
            krasu_skaits[krasa] += 1
        else:
            krasu_skaits[krasa] = 1
    
    print("Dzīvnieku krāsas un to skaits:")
    for krasa, skaits in krasu_skaits.items():
        print(f"{krasa}: {skaits}")

# Testēšana
fails = "dzivnieki.json"
dzivnieki = nolasi_dzivniekus(fails)
analize_dzivnieku_sugu(dzivnieki)
analize_dzivnieku_krasu(dzivnieki)
