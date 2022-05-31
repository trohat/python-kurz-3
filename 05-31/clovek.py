class Motor:
    def __init__(self, objem, vykon):
        self.objem = objem
        self.vykon = vykon

    def __str__(self):
        return f"Motor o objemu {self.objem}."

motor1 = Motor(1.6, 120)
motor_silny = Motor(2, 135)
motor_slaby = Motor(1.3, 85)

class Auto:
    def __init__(self, znacka, barva, motor):
        self.znacka = znacka
        self.barva = barva
        self.motor = motor

    def __str__(self):
        return f"{self.barva.capitalize()} {self.znacka}"


bourak = Auto("Mercedes", "růžový", motor_silny)

rachotina = Auto("Moskvič", "modrý", motor_slaby)

rodinne_auto = Auto("Škodovka", "červená", motor1)

print(rodinne_auto)


class Clovek:
    def __init__(self, jmeno, povolani, vek, auto):
        self.jmeno = jmeno
        self.povolani = povolani
        self.vek = vek
        self.auto = auto

    def vstavej(self):
        print("Můžu ještě chvíli spát???")

    def __str__(self):
        return self.jmeno


adam = Clovek("Adam", "strojvůdce", 31, rachotina)
eva = Clovek("Eva", "moderátorka", 25, bourak)

print(adam)
print(adam.vek)
print(adam.povolani)

print(adam.auto)
print(eva.auto)
print(bourak)

adam.auto = rodinne_auto

print(adam.auto.znacka)

print(motor_slaby)

print(rachotina.motor)
print(rachotina.motor.vykon)
print(eva.auto.motor.objem)
