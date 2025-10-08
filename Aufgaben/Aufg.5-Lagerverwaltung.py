# Lagerverwaltung 

lager = [
    {"produkt_id": 101, "name": "SSD 1TB", "lagerbestand": 15},
    {"produkt_id": 102, "name": "SSD 2TB", "lagerbestand": 12},
    {"produkt_id": 104, "name": "SSD 4TB", "lagerbestand": 10}
    ]

print("")

y = []

for x in lager:
    print(f"Produkt: {x["name"]}, Aktueller Bestand: {x["lagerbestand"]}")
    y.append(x["lagerbestand"]*50)

print("")

gesamter_warenwert = sum(y)

print(f"Der gesamte Warenwert beträgt: {gesamter_warenwert} Euro")
print("")
