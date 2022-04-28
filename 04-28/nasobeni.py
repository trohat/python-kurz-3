
def nasobeni(prvni_cislo, druhe_cislo):
    vysledek = prvni_cislo * druhe_cislo
    return vysledek

def nasobeni_verze_dva(prvni_cislo, druhe_cislo):
    return prvni_cislo * druhe_cislo
    
print(nasobeni(5, 6))

vysledek_nasobeni_petky_a_sestky = nasobeni(5, 6)

print(nasobeni(8, 7))

vysledek_nasobeni_sedmicky_a_osmicky = nasobeni(8, 7)

konecny_vysledek = nasobeni(vysledek_nasobeni_petky_a_sestky, vysledek_nasobeni_sedmicky_a_osmicky)

print("Na příštím řádku je úplný výsledek našeho výpočtu...")
print(konecny_vysledek)