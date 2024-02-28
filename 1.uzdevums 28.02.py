import csv

def salidzini_csv(csv1, csv2):

    saraksts_csv1 = []
    saraksts_csv2 = []

    with open(csv1, 'r') as fail1:
        lasitajs_csv1 = csv.reader(fail1)
        for rinda in lasitajs_csv1:
            saraksts_csv1.append(rinda)

    with open(csv2, 'r') as fail2:
        lasitajs_csv2 = csv.reader(fail2)
        for rinda in lasitajs_csv2:
            saraksts_csv2.append(rinda)

    garums_csv1 = len(saraksts_csv1)
    garums_csv2 = len(saraksts_csv2)

    if garums_csv1 == garums_csv2:
        print("Ir vienādi!")
    else:
        diference = abs(garums_csv1 - garums_csv2)
        print(f"Sarakstu garumu diference: {diference}")

csv_failu_nosaukums_1 = "csv1.csv"
csv_failu_nosaukums_2 = "csv2.csv"
salidzini_csv(csv_failu_nosaukums_1, csv_failu_nosaukums_2)