print("Kalkulačka, co toho umí fakt hodně - umí dělit dvě čísla!!")
print("To je ale chytrá kalkulačka, co???")

cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))

if cislo2 != 0:
    vysledek = cislo1 / cislo2
    print("Výsledek je:", vysledek)
else:
    print("Nulou nelze dělit... :((")



