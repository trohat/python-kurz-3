print("Kalkulačka, co toho umí fakt hodně - umí dělit dvě čísla!!")
print("To je ale chytrá kalkulačka, co???")

try:
    cislo1 = int(input("Zadej první číslo: "))
    cislo2 = int(input("Zadej druhé číslo: "))

    vysledek = cislo1 / cislo2

    print("Výsledek je:", vysledek)

except ZeroDivisionError:
    print("Nelze dělit nulou")

except ValueError:
    print("Zadal jsi něco, co není číslo...")

except:
    print("Vznikla neznámá chyba...")

print("Program bez problémů pokračuje")
