
for promenna in range(10):
    if promenna == 5:
        print("Teď nic nebude, popojedeme dál...")
        continue
    if promenna == 7: 
        print("Končíme úplně")
        break
    print("Uvnitř cyklu")
    print(promenna)

print("Tady cyklus skončil...")

for pismeno in "ahoj":
    print(pismeno)
    