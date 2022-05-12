dest_ve_mestech = {}

while True:
    mesto = input("Zadej město (nebo prázdný řádek pro ukončení): ")
    if mesto == "":
        break
    mm_srazek = int(input("Zadej, kolik napršelo: "))
    
    if mesto in dest_ve_mestech:
        dest_ve_mestech[mesto]["mm_srazek"] += mm_srazek
        dest_ve_mestech[mesto]["pocet_mereni"] += 1
    else:
        dest_ve_mestech[mesto] = {
            "mm_srazek": mm_srazek,
            "pocet_mereni": 1
        }
    
    #dest_ve_mestech[mesto] = dest_ve_mestech.get(mesto, 0) + mm_srazek

for mesto, data in dest_ve_mestech.items():
    print(f"Ve městě {mesto} napršelo průměrně {data['mm_srazek'] / data['pocet_mereni']} mm srážek.")

print(dest_ve_mestech)

