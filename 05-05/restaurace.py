#způsob vyhledávání proměnných
#LEGB = local, enclosing, global, built-in

menu = {
    "řízek": 80,
    "polévka": 30,
    "salát": 50,
    "brambory": 20,
    "zákusek": 40,
    "pivo": 40,
    "víno": 45,
    "limonáda": 30,
    "čaj": 35
}

del menu["čaj"]


def objednavka():
    print("Vítejte v našíx restauraci.")
    print("Můžete začít s objednáváním.")
    print("Pokud zadáte prázdnou objednávku, objednávání se tím ukončí.")
    celkova_cena = 0
    while True:
        jidlo = input("Co by sis dal k jídlu nebo k pití? ")
        if jidlo == "":
            break
        if jidlo in menu:
            cena = menu[jidlo]
            print("Cena tvého jídla je", cena)
            celkova_cena += cena
        else:
            print("Takovou blbost nemáme.")
    print("Děkujeme za objednávku.")
    print("Celková cena tvé objednávky je", celkova_cena)

objednavka()