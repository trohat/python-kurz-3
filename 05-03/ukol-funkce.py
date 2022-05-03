
def soucet_cisel_v_rozsahu(zacatek, konec):
    if konec <= zacatek:
        return 
    
    pomocna_promenna = 0
    for cislo in range(zacatek + 1, konec):
        pomocna_promenna += cislo

    return pomocna_promenna
    
vysledek = soucet_cisel_v_rozsahu(5, 8)
print(vysledek)

# KAŽDÝ NOVÝ KÓD TESTUJTE, A TO POŘÁDNĚ!!!
assert soucet_cisel_v_rozsahu(1, 10) == 44
assert soucet_cisel_v_rozsahu(0, 11) == 55
assert soucet_cisel_v_rozsahu(13, 15) == 14
assert soucet_cisel_v_rozsahu(22, 25) == 47
assert soucet_cisel_v_rozsahu(5, 7) == 10