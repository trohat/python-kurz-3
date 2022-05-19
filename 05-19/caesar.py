

def caesar_cipher(retezec, posun):
    novy_retezec = ""
    for pismeno in retezec:
        cislo = ord(pismeno)
        if (cislo >= 97 and cislo <= 122) or (cislo >= 65 and cislo <= 90):
            cislo += posun
            if (cislo > 122) or (pismeno.isupper() and cislo > 90):
                cislo = cislo - 26
            nove_pismeno = chr(cislo)
            novy_retezec += nove_pismeno
        else:
            novy_retezec += pismeno
    return novy_retezec

print(caesar_cipher("AHOJ Pavle a Zuzko", 0))
print(caesar_cipher("AHOJ Pavle a Zuzko", 1))
print(caesar_cipher("AHOJ Pavle a Zuzko", 2))
print(caesar_cipher("AHOJ Pavle a Zuzko", 3))
print(caesar_cipher("AHOJ Pavle a Zuzko", 4))
print(caesar_cipher("AHOJ Pavle a Zuzko", 5))
print(caesar_cipher("AHOJ Pavle a Zuzko", 6))
