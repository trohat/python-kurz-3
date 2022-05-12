pocasi = {
    20: "slunecno",
    21: "deštivo",
    22: "vítr",
    23: "vedro",
    24: "kroupy",
    25: "strašný vedro",
    26: "zima"
}

datum = int(input("Zadej datum: "))

print(f"Dnes bude {pocasi[datum]}.")
print(f"Zítra bude {pocasi[datum + 1]}.")
print(f"Pozítří bude {pocasi[datum + 2]}.")