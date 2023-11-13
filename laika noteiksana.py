#Laika noteiksana

import requests

URL = "https://worldtimeapi.org/timezone/Europe/Riga"

dati = requests.get(URL)

print(dati)

laiksLatvija = dati.json()

print(laiksLatvija)

print(laiksLatvija(["utc_datetime"]))