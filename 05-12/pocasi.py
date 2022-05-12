dest_ve_mestech = {}

pocet_mereni = {}

while True:
    mesto = input("Zadej město (nebo prázdný řádek pro ukončení): ")
    if mesto == "":
        break
    mm_srazek = int(input("Zadej, kolik napršelo: "))
    
    if mesto in dest_ve_mestech:
        dest_ve_mestech[mesto] += mm_srazek
        pocet_mereni[mesto] += 1
    else:
        dest_ve_mestech[mesto] = mm_srazek
        pocet_mereni[mesto] = 1
    
    #dest_ve_mestech[mesto] = dest_ve_mestech.get(mesto, 0) + mm_srazek

for mesto, srazky in dest_ve_mestech.items():
    print(f"Ve městě {mesto} napršelo průměrně {srazky / pocet_mereni[mesto]} mm srážek.")

