#The user types in two numbers. Find the sum and average
#of numbers in the specified range.

cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo (musí být větší než první): "))

if cislo2 < cislo1:
    pomocna = cislo1
    cislo1 = cislo2
    cislo2 = pomocna

soucet = 0
pocet = 0

for i in range(cislo1 + 1, cislo2):
    soucet = soucet + i
    pocet = pocet + 1

print("Součet je", soucet)

print("Průměr je", soucet / pocet)
