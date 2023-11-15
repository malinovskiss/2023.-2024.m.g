import requests
import json

URL = "https://itunes.apple.com/search?entity=song&limit=22&term=brainstorm"

atbilde = requests.get(URL)

print (atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))

for a in dati["results"]:
    print(a["trackName"])