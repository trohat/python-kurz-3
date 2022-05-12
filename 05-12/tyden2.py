pocasi = {
    "pondělí": "slunecno",
    "úterý": "deštivo",
    "středa": "vítr",
    "čtvrtek": "vedro",
    "pátek": "kroupy",
    "sobota": "strašný vedro",
    "neděle": "zima"
}

seznam_dni = list(pocasi.keys())
print(seznam_dni)

datum = input("Zadej datum jménem dne: ")

if not datum in seznam_dni:
    raise Exception("Daný den neexistuje!")

index = seznam_dni.index(datum)
zitra = seznam_dni[(index + 1) % 7]
pozitri = seznam_dni[(index + 2) % 7]


print(f"Dnes bude {pocasi[datum]}.")
print(f"Zítra bude {pocasi[zitra]}.")
print(f"Pozítří bude {pocasi[pozitri]}.")
