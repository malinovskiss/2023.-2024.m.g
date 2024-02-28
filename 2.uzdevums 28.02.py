import json

def apvienot_un_salidzinat_json(json1, json2, rezultata_faila_nosaukums):

    with open(json1, 'r') as fail1:
        vardnicas_json1 = json.load(fail1)

    with open(json2, 'r') as fail2:
        vardnicas_json2 = json.load(fail2)

    apvienota_vardnica = {**vardnicas_json1, **vardnicas_json2}

    with open(rezultata_faila_nosaukums, 'w') as rezultata_faila:
        json.dump(apvienota_vardnica, rezultata_faila, indent=2)

    atslegas_vienā_vardnica = set(vardnicas_json1.keys()) | set(vardnicas_json2.keys())
    print("Atslēgas, kas atrodas vienā no vārdnīcām:", atslegas_vienā_vardnica)

    atslegas_abas_vardnicas = set(vardnicas_json1.keys()) & set(vardnicas_json2.keys())
    print("Atslēgas, kas atrodas abās vārdnīcās:", atslegas_abas_vardnicas)

json_failu_nosaukums_1 = "json1.json"
json_failu_nosaukums_2 = "json2.json"
rezultata_faila_nosaukums = "rezultats.json"
apvienot_un_salidzinat_json(json_failu_nosaukums_1, json_failu_nosaukums_2, rezultata_faila_nosaukums)