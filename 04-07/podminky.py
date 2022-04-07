
pocet_navstev = 3
karta_staleho_zakaznika = True

if pocet_navstev >= 10:
    print("Máme pro vás velmi výhodné ceny letenek")
    print("Ale pozor, máme už jen poslední kusy...")
    print("Rychle objednávejte!")
    cena_letenky = 10000
    if karta_staleho_zakaznika == True:
        print("Nabízíme vám luxusní občerstení na palubě.")
        print("")
        print("")
        if 15 > 5:
            print("Umíme matematiku...")
    else:
        print("Nechcete si pořídit kartu stálého zákazníka?")
        
elif pocet_navstev >= 5:
    print("Jsme rádi, že se vracíte")
    print("Máme pro vás velmi výhodné ceny letenek")
    cena_letenky = 6500
elif pocet_navstev >= 2:
    print("Jsme rádi, že se vracíte")
    cena_letenky = 5000
else:
    print("Vítáme vás")
    print("Pohodlně se posaďte")
    print("Dovolte, abychom vám představili naši společnost")
    cena_letenky = 4000

if 20 + 3 > 10:
            print("Další příklad z matematiky, hurá!!!")
print("Nastupujte do letadla")

