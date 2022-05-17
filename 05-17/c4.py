lidi = ["pavel", "petr", "jana", "klára", "prokop", "kryštof", "marian", "petra"]

lidi_spravne = []

for jmeno in lidi:
    if jmeno.startswith("p"):
        lidi_spravne.append(jmeno.capitalize())

print(lidi_spravne)

lidi3 = [
    jmeno.capitalize()
    for jmeno in lidi
    if jmeno.startswith("p")
]

lidi4 = [jmeno for jmeno in lidi if not jmeno.startswith("p")]

print(lidi3)
print(lidi4)