seznam = [-2, 3, 5, -1, 7, 8, 9, -3]

slovnik = {
    cislo : cislo * cislo
    for cislo in seznam
    if cislo > 0
}

print(slovnik)
