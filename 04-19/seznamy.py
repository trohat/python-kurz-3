seznam = []

for i in range(50):
    seznam.append(i)

s1 = seznam[10:15]
s2 = seznam[23:27]
s3 = seznam[35:40]
vysledek = s1 + s2 + s3

print(vysledek)


zvirata = ["opice", "kočka", "myš", "slon", "buvol", "surikata"]

try:
    zvirata.index("mrakodrap")
except ValueError:
    print("Došlo k chybě, mrakodrap nebyl nalezen")

if "mrakodrap" in zvirata:
    index_mrakodrapu = zvirata.index("mrakodrap")
else:
    index_mrakodrapu = -1