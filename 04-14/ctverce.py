#****
#****
#****
#****

delka_strany = int(input("Zadej délku strany čtverce: "))

znak = "*"
jedna_strana = znak * delka_strany 
jedna_strana_cely_radek = jedna_strana + "\n"

ctverec = jedna_strana_cely_radek * delka_strany

print(ctverec)

print("Zde bude čtverec vytvořený kódem na jednu řádku...")
print(("*" * delka_strany + "\n") * delka_strany)

print("Zde bude čtverec vytvořený pomocí cyklu...")

for i in range(delka_strany): # řádky
    for j in range(delka_strany): # sloupce
        print("*", end="")
    print()

print("Zde je kombinace obou postupů")
for i in range(delka_strany): # řádky
    print ("*" * delka_strany)  

print("Zde bude dutý čtverec")
posledni = delka_strany - 1
for i in range(delka_strany): # řádky
    for j in range(delka_strany): # sloupce
        if i == 0 or j == 0 or i == posledni or j == posledni:
            print("@", end="")
        else:
            print(" ", end="")
    print()

print("Zde bude druhý dutý čtverec")
for i in range(delka_strany): # řádky
    if i == 0 or i == delka_strany - 1:
        print("*" * delka_strany)
    else:
        print("*" + " " * (delka_strany - 2) + "*")
