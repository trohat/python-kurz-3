from pprint import pprint
# slovníky, neboli dictionaries, neboli dicts

pes = {
    "jmeno": "Alík",
    "barva": "hnědá",
    "váha": 5 * 6 + 30,
    "plemeno": "vlčák",
    "umí hlídat": True,
    "jméno majitele": "Adam",
}

print(pes["jmeno"])

print(pes["jméno majitele"])

pes["jmeno"] = "Rex"

print(pes["jmeno"])

pes["povaha"] = "hodnej, rád se mazlí"

print(pes["povaha"])

pprint(pes)

anglictina = {
    "dveře": "door",
    "stůl": "table",
    "židle": "chair",
    "dům": "house",
    "pes": "dog"
}

print(anglictina["dveře"])
print("stůl" in anglictina)
print("koupelna" in anglictina)

anglictina["pes"] = "cat"
anglictina["ryba"] = "fish"

print(anglictina)

for klic in anglictina.keys():
    print(klic)

nakupni_seznam = {
    "rohliky": 20,
    "mléko": 17,
    "máslo": 65,
    "maso": 100,
    "mrkev": 19
}

print("V nákupu bude:")

for polozka in nakupni_seznam.keys():
    print(polozka)

print("Ceny budou:")

celkovy_nakup = 0

for cena in nakupni_seznam.values():
    celkovy_nakup += cena
    print(cena)

print(f"Celková cena nákupu je {celkovy_nakup}")

for polozka, cena in nakupni_seznam.items():
    print(f"Kup {polozka}, bude to stát {cena} Kč.")

