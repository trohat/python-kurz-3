prihlasovaci_udaje = {
    "Adam": "1234",
    "Boris": "5678",
    "Cyril": "123456"
}

pocet_pokusu = 0
while True:
    uzivatelske_jmeno = input("Zadej své uživatelské jméno: ")
    heslo = input("Zadej heslo: ")
    if uzivatelske_jmeno in prihlasovaci_udaje:
        spravne_heslo = prihlasovaci_udaje[uzivatelske_jmeno]
        if heslo == spravne_heslo:
            print("Podařilo se ti správně přihlásit...")
            print("Pokračuješ dále do aplikace.")
            login_uspesny = True
            break
        else:
            print("Máš špatné heslo")
    else:
        print("Máš špatné uživatelské jméno")
    pocet_pokusu += 1
    if pocet_pokusu > 5:
        login_uspesny = False
        print("Tvé přihlášení bylo neúspěšné, vyčerpal jsi všechny pokusy.")
        break