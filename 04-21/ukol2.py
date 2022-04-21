#14.) Vypočítejte průměr čísel v seznamu.

seznam = [5, 7, 8, 9, 15, 25, 34, 46]

soucet = 0
#pocet = 0

for cislo in seznam:
    soucet += cislo
    #pocet += 1


print("Průměr čísel v seznamu je", soucet/ len(seznam))