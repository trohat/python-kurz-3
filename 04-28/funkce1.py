def pozdrav(jmeno, drink):
    print(f"ahoj, vítám tě, člověče jménem {jmeno}")
    print("odlož si věci do šatny")
    print(f"na baru je pro tebe připravený {drink}")
    print(f"poznáš ho tak, že je na něm nálepka {jmeno}")



jmeno_hosta = input("Jak se jmenuješ?")
oblibeny_napoj = input("Co rád/a piješ?")

pozdrav(jmeno_hosta, oblibeny_napoj)

jmeno_hosta = input("Jak se jmenuješ?")
pozdrav(jmeno_hosta, "rum")


"""
pozdrav("Petr", "rum")
pozdrav("Anička", "víno")
pozdrav("Tomáš", "whiskey")
pozdrav("Andy", "metaxa")
"""