lager=[
    {"produkt_id":101,"name":"Tastatur","lagerbestand":10},
    {"produkt_id":102,"name":"Maus","lagerbestand":25},
    {"produkt_id":103,"name":"Monitor","lagerbestand":5},
]
preis=0
for produkt in lager:
    print(f"Produkt: {produkt["name"]}")
    print(f"Aktueller Bestand: {produkt["lagerbestand"]}")
    preis=preis+produkt["lagerbestand"]*50
    print("----------------------")
print(f"Der gesamte Warenwert bertägt: {preis} €")