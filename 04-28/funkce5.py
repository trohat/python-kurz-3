def kalkulacka():
    print("Program KALKULAČKA")
    operace = int(input("Zadej, co chceš počítat: 1 - sčítání, 2 - násobení: "))
    cislo1 = int(input("Zadej první číslo: "))
    cislo2 = int(input("Zadej druhé číslo: "))
    if operace == 1:
        vysledek = cislo1 + cislo2
        print(f"Součet čísel {cislo1} a {cislo2} je {vysledek}.")
    elif operace == 2:
        vysledek = cislo1 * cislo2
        print(f"Součin čísel {cislo1} a {cislo2} je {vysledek}.")
    else:
        print("Toto je neplatná operace.")


kalkulacka()