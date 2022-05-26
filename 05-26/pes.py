
class Pes:
    def __init__(self, jmeno, rasa):
        self.jmeno = jmeno
        self.rasa = rasa

    def stekej(self):
        print("haf haf haf")

    def __str__(self):
        return f"Ahoj, já jsem {self.rasa} {self.jmeno}."


alik1 = Pes("Alík", "labrador")

print(alik1)
print(alik1.jmeno)
print(alik1.rasa)

alik1.jmeno = "Rex"
print(alik1.jmeno)

alik1.stekej()

babiccin_pes = Pes("Max", "pudlík")
dedeckuv_pes = Pes("Hugo", "vlčák")
souseduv_pes = Pes("Filip", "bernardýn")
sousedcin_pes = Pes("Monty", "jezevčík")

dedeckuv_pes.stekej()
souseduv_pes.stekej()
sousedcin_pes.stekej()

print(babiccin_pes.jmeno)
print(babiccin_pes.rasa)
print(dedeckuv_pes.jmeno)
print(dedeckuv_pes.rasa)
print(souseduv_pes.jmeno)
print(sousedcin_pes.rasa)

print(sousedcin_pes)
