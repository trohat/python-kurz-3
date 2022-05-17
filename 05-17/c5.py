seznam = [[1, 2, 3], [4, 6, 7], [8, 3, 9]]

novy_seznam = []

for vnitrni in seznam:
    for cislo in vnitrni:
        novy_seznam.append(cislo * cislo)

print(novy_seznam)

seznam2 = [cislo * cislo for vnitrni in seznam for cislo in vnitrni]

print(seznam2)

