class Clovek:
    pocet_vytvorenych_lidi = 0

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.__class__.pocet_vytvorenych_lidi += 1

    @staticmethod
    def vytiskni_pocet_lidi_staticky():
        return f"Už bylo vytvořeno {Clovek.pocet_vytvorenych_lidi} lidí. - statická metoda"

    @classmethod
    def vytiskni_pocet_lidi_pomoci_classmethod(cls):
        return f"Už bylo vytvořeno {cls.pocet_vytvorenych_lidi} lidí. - třídní metoda"

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

adam = Clovek("Adam", "Novák")
karel = Clovek("Karel", "Černý")
#filip = Clovek("Filip", "Novotný")

#print(Clovek.pocet_vytvorenych_lidi)
print(Clovek.vytiskni_pocet_lidi_staticky())
print(Clovek.vytiskni_pocet_lidi_pomoci_classmethod())
