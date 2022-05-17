def secti(retezec):
    seznam = retezec.split()
    novy_seznam = [
        int(prvek)
        for prvek in seznam
        if prvek.isdigit()
    ]
    soucet = sum(novy_seznam)
    return soucet

print(secti("10 abc 20 de44 30 55fg 40"))

def secti_kratka(retezec):
    return sum(
        int(prvek)
        for prvek in retezec.split()
        if prvek.isdigit()
    )
