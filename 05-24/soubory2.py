soubor = open("ovoce.txt", encoding="utf-8")

for line in soubor:
    print(line, end="")

soubor.close()