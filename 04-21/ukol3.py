#13.) Najděte maximální číslo v seznamu bez použití funkce max.

seznam = [5, 72, 45, 88, 91, 15, 25, 34, 46]

print("Maximum pomocí vestavěné funkce Pythonu:", max(seznam))
print("Minimum pomocí vestavěné funkce Pythonu:", min(seznam))

max_cislo = seznam[0]
min_cislo = seznam[0]

for cislo in seznam:
    if cislo > max_cislo:
        max_cislo = cislo
    elif cislo < min_cislo:
        min_cislo = cislo

print("Maximum ručně je:", max_cislo)
print("Minimum ručně je:", min_cislo)