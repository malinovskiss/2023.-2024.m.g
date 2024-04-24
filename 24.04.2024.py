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
