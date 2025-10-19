# Lagerverwaltung-2


def drucke_produkt_info(produkt):
    print("Produkt:", produkt["name"], ", Aktueller Bestand:", produkt["lagerbestand"], "Stück")
    
def berechne_gesamtlagerwert(lager):
    gesamtwert = 0
    for produkt in lager:
        gesamtwert = gesamtwert+produkt["lagerbestand"]*75
    return gesamtwert


lager = [
	{"produkt_id": 101, "name": "SSD 1TB", "lagerbestand": 35},
	{"produkt_id": 102, "name": "RAM 16GB", "lagerbestand": 50},
	{"produkt_id": 103, "name": "CPU i7", "lagerbestand": 20}
	]

print("")

for produkt in lager:
    drucke_produkt_info(produkt)

wert = berechne_gesamtlagerwert(lager) 

print(f"\nDer Gesamtwert der Lagerbestände beträgt: {wert} Euro")
print("")
