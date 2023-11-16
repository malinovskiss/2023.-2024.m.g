import requests
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

atbilde = requests.get(URL)

# print (atbilde)

dati = atbilde.json()
#print(dati)
print(json.dumps(dati,indent = 4))
#vvsk = {"sakumskola":
#           {"1":{
#               'a':{"vards":"Pēteris","uzvards":"Bērziņš"},
#               'b':{"vards":"Pēteris","uzvards":"Bērziņš"}},
#             "2":},
#       "pamatskola":}
USD = dati['bpi']['USD']
print(USD)
USD = dati['bpi']['USD']['rate_float'] #Dabujam bitkoinu cenu USD valuta 
print(USD)
ievade = input("Ievadi bitkoinu daudzumu: ")
matematiskaDarbiba = USD * float(ievade)
print(f"{ievade} bitkoinu maksa {matematiskaDarbiba}$")
