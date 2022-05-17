seznam = [2, 3, 2, 3, 4, 1, 0, 9, 8, 8, 2, 2]

#SET COMPREHENSION
novy_seznam = {
    cislo + 10
    for cislo in seznam
}

print(novy_seznam)

