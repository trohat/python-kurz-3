#f-stringy

cislo = 5
cislo2 = 6

vysledek = cislo * cislo2

print("Číslo", cislo, "násobené číslem", cislo2, "dává výsledek", vysledek, ".")
print("Číslo " + str(cislo) + " násobené číslem " + str(cislo2) + " dává výsledek " + str(vysledek) + ".")

# tohle je takzvaný f-string
print(f"Číslo {cislo} násobené {cislo2} něco dává výsledek {vysledek}.")

slovo = "slon"

print(f"Dvakrát šest je {2*6} a {slovo} velkými písmeny je {slovo.upper()}.")

