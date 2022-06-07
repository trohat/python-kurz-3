# DĚDIČNOST

class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def jdi_do_prace(self):
        print("Těším se, jaké nové hodnoty dnes vytvořím.")

    def jdi_do_hospody(self):
        print("Dám si pět piv.")

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Programator(Clovek):
    def __init__(self, jmeno, prijmeni, jazyk):
        super().__init__(jmeno, prijmeni)
        self.jazyk = jazyk

    def programuj(self):
        print("Použiju dnes cyklus for nebo while?")

    def jdi_do_hospody(self):
        super().jdi_do_hospody()
        print("Je lepší Python nebo Java? V hospodě to vyřešíme.")

    def __str__(self):
        return f"Rád programuji v jazyce {self.jazyk}"

class Manazer(Clovek): 
    def vyhod_zamestnance(self):
        print("Tak koho dnes vyhodíme?? :)")

    def jdi_do_hospody(self):
        print("Dnes v hospodě probereme výsledky za minulý měsíc.")

karel = Clovek("Karel", "Novák")
jakub = Programator("Jakub", "Starosta", "Python")
michal = Manazer("Michal", "Novotný")

lidi = [karel, jakub, michal]

for clovek in lidi:
    print()
    print(clovek)
    clovek.jdi_do_hospody()

