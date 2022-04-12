#The user types in the number of meters. Based on the
#user’s choice, the program converts meters to miles, inches,
#or yards.

metry = int(input("Zadej počet metrů: "))

print("Na co chceš převádět?")
print("k = kilometry, c = centimetry, m = milimetry")
volba = input("Tak co to bude? ")

#print(metry, volba)

if volba == "k":
    vysledek = metry / 1000
    print("Vyšlo", vysledek, "kilometrů.")
elif volba == "c":
    vysledek = metry * 100
    print("Vyšlo", vysledek, "centimetrů.")
elif volba == "m":
    vysledek = metry * 1000
    print("Vyšlo", vysledek, "milimetrů.")
else:
    print("Zadal jsi neplatnou volbu, zkus to příště znovu...")