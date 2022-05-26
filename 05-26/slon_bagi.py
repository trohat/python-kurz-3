class Slon:
    def __init__(self, jmeno, barva, vaha, povolani):
        self.jmeno = jmeno
        self.barva = barva
        self.vaha = vaha
        self.povolani = povolani
    
    def troubit(self):
        print(f"Slon {self.jmeno} trouba moc nahlas")

    def strikat(self):
        return f"Slon {self.jmeno} zacal strikat vodu na kolemjdouci"
    
    def usmev(self):
        return "Ja si usmivam"

stary_slon = Slon("Harfa", "seda", "4.5tun", "herec")
mlady_slon = Slon("John", "tmava_seda", "2tun", "roztomily")
dospely_slon = Slon("Xavier", "hneda", "5tun", "drsnak")
mila_slon = Slon("mona", "ruzova", "3tun", "mila")

slony = [stary_slon, mlady_slon, dospely_slon, mila_slon]


stary_slon.troubit()
print(dospely_slon.strikat())

print(stary_slon.jmeno)

stary_slon.jmeno = "Dada"
print(stary_slon.jmeno)

print(mlady_slon.povolani)


for slon in slony:
    if slon.barva != "ruzova":
        print(slon.strikat())
    else:
        print(slon.usmev())