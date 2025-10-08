# FUNKTIONEN DEFINIEREN

def drucke_produkt_info(produkt):
    """
    Nimmt ein Produkt-Dictionary entgegen und gibt dessen
    Name und Lagerbestand formatiert aus. (Keine Schleife nötig)
    """
    name = produkt["name"]
    bestand = produkt["lagerbestand"]
    
    print(f"Produkt: {name}, Aktueller Bestand: {bestand} Stück")


def berechne_gesamtlagerwert(lager_liste):
    """
    Berechnet den Gesamtwert des Lagers ohne eine for-Schleife
    durch manuellen Zugriff auf die ersten drei Listenelemente.
    """
    gesamtwert = 0
    fester_preis = 75  # Fester Preis in Euro

    # Produkt 1: Zugriff über Index [0]
    bestand_1 = lager_liste[0]["lagerbestand"]
    gesamtwert = gesamtwert + (bestand_1 * fester_preis)
    
    # Produkt 2: Zugriff über Index [1]
    bestand_2 = lager_liste[1]["lagerbestand"]
    gesamtwert = gesamtwert + (bestand_2 * fester_preis)
    
    # Produkt 3: Zugriff über Index [2]
    bestand_3 = lager_liste[2]["lagerbestand"]
    gesamtwert = gesamtwert + (bestand_3 * fester_preis)
        
    return gesamtwert


# HAUPTPROGRAMM 

# Definieren der 'lager'-Liste
lager = [
    {"produkt_id": 101, "name": "SSD 1TB", "lagerbestand": 35},
    {"produkt_id": 102, "name": "RAM 16GB", "lagerbestand": 50},
    {"produkt_id": 103, "name": "CPU i7", "lagerbestand": 20}
]

print("--- LAGERBESTAND BERICHT ---")


for artikel in lager:
    drucke_produkt_info(artikel)

# Rufen Sie die Berechnungsfunktion auf
finaler_gesamtwert = berechne_gesamtlagerwert(lager)

print("\n--- ZUSAMMENFASSUNG ---")
print(f"Der gesamte Warenwert des Lagers beträgt: {finaler_gesamtwert:.2f} Euro.")