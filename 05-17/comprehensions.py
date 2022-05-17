seznam = [5, 6, 9, 8, 4, 3, 2, 1]

seznam_na_druhou = []

for cislo in seznam:
    seznam_na_druhou.append(cislo * cislo)

print(seznam_na_druhou)

novy_seznam_na_druhou = [cislo * cislo for cislo in seznam]

novy_seznam_3 = [
    cislo + 5 
    for cislo in seznam
]

print(novy_seznam_na_druhou)