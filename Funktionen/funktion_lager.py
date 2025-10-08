lager=[
    {"produkt_id":101,"name":"Tastatur","lagerbestand":10},
    {"produkt_id":102,"name":"Maus","lagerbestand":25},
    {"produkt_id":103,"name":"Monitor","lagerbestand":5},
]
def drucke_produkt_info(produkt):
    print(f"Produkt: {produkt["name"]}, Aktueller Bestand: {produkt["lagerbestand"]} Stück")
 
def berechne_gesamtlagerwert(lager):
    gesamtwert=0

    for produkt in lager:
        gesamtwert=gesamtwert+produkt["lagerbestand"]*75
    return gesamtwert
        
for produkt in lager:
    drucke_produkt_info(produkt)
wert=berechne_gesamtlagerwert(lager)
print(f"Der Lagerbestandswert beträgt: {wert} €")