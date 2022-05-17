seznam = [5, -6, 9, -8, 4, -3, -2, 1]

novy_seznam = []

for cislo in seznam:
    if cislo >= 0:
        novy_seznam.append(cislo * cislo)

print(novy_seznam)

seznam2 = [
    cislo * cislo
    for cislo in seznam
    if cislo >= 0
]

seznam3 = [cislo * cislo for cislo in seznam if cislo >= 0]
