class Papousek:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva

    def __str__(self):
        return f"{self.barva} {self.jmeno}"

ara = Papousek("Rudolf", "žlutý")
arara = Papousek("Pepa", "fialovorůžový")
jiny_papousek = Papousek("Ferda", "modrý")
muj_papousek = Papousek("Tonda", "strakatý")

class Klec:
    def __init__(self):
        self.papousci = []

    def pridej_papouska(self, papousek):
        if isinstance(papousek, Papousek):
            self.papousci.append(papousek)
        else:
            print(f"{papousek} - tohle není papoušek, to nemá v kleci co dělat...")

    def vyndej_papouska(self, papousek):
        if papousek in self.papousci:
            self.papousci.remove(papousek)
        else:
            print(f"{papousek} není v kleci")

    def __str__(self):
        if len(self.papousci) == 0:
            return "Prázdná klec"
        vysledek = "Klec a v ní je "
        for papousek in self.papousci:
            vysledek += str(papousek) + " a "
        return vysledek[:-3]

drevena_klec = Klec()

print(drevena_klec)

drevena_klec.pridej_papouska(ara)
drevena_klec.pridej_papouska(arara)
drevena_klec.pridej_papouska(muj_papousek)
drevena_klec.pridej_papouska("stará guma od auta")

print(drevena_klec)

drevena_klec.vyndej_papouska(arara)
drevena_klec.vyndej_papouska(jiny_papousek)
drevena_klec.vyndej_papouska("nová guma")


print(drevena_klec)

# zapouzdření