#13.) Vypočítejte součet čísel v seznamu bez použití funkce sum.

seznam = [5, 7, 8, 9, 15, 25, 34, 46]

print("Výsledek pythonovskou funkcí je", sum(seznam))

vysledek = 0

#for index in range(len(seznam)):
#    print(seznam[index])

for cislo in seznam:
    vysledek += cislo


print("Výsledek ručně je", vysledek)