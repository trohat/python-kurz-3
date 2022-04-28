def scitani(a, b):
    vysledek = a + b
    return f"Součet čísel {a} a {b} je {vysledek}."

print("Program KALKULAČKA")
cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))

vysledek_funkce = scitani(cislo1, cislo2)

print(vysledek_funkce)