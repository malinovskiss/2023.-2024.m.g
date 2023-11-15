import requests
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

atbilde = requests.get(URL)

print (atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))

for a in dati:
    print(a["USD"])