
lidi = ["pavel", "petr", "jana", "klára", "prokop", "kryštof", "marian", "petra"]

lidi_spravne = []

for jmeno in lidi:
    lidi_spravne.append(jmeno.capitalize())

print(lidi_spravne)

lidi2 = [jmeno.capitalize() for jmeno in lidi]

print(lidi2)
