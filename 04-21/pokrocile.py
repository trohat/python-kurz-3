#pokročilé operace se seznamem
#pouze pro vážné zájemce
# otázka, kterou zde řešíme, byla:
# jak předělat seznam stringů na seznam intů
seznam = ["20", "30", "40", "56", "89"]

novy_seznam = []

#jednoduchý postup, která ale musíte URČITĚ znát
for cislo in seznam:
    novy_seznam.append(int(cislo))

#list comprehension - velmi oblíbená, budeme ještě probírat
novy3 = [int(cislo) for cislo in seznam]

# funkce map, častá třeba v JS, v Pythonu se používá 
# méně často - probírat nebudeme
novy2 = map(int, seznam)


