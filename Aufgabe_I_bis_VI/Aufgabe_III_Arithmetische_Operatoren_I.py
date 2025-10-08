#Aufgabe 1: Zinsberechnung
#Erstellen Sie eine neue Anwendung. Definiere die Variablen, um die Zinsen für ein Jahr auszurechnen

kapital = 1647
zinssatz = 3
laufzeit = 1

zinsen= kapital*zinssatz / 100*laufzeit
print(f"Die Zinsen nach {laufzeit} Jahr(en) betragen: {zinsen:.2f} Euro")




#Aufgabe 2: Energieverbrauch
strompreis = 0.30

verbrauch_fernseher = 3 * 1 * 3 * 365
verbrauch_herd= 2 * 2 * 4 * 52
verbrauch_router= 2 * 4 * 365
verbrauch_heizung= 8 * 20 * 170

gesamtverbrauch= verbrauch_fernseher + verbrauch_herd + verbrauch_router + verbrauch_heizung
kosten= gesamtverbrauch * strompreis

print(f"Gesamtverbrauch in kWh/Jahr: {gesamtverbrauch}")
print(f"Stromkosten pro Jahr: {kosten:.2f} Euro")




#Aufgabe 3: Druckerberger
netto = 120
Wartesteuer = 0.07  #7% als Dezimalzahl

gesamtwert= netto * (1 + Wartesteuer)
print(f"Burak muss insgesamt {gesamtwert:.2f} Euro bezahlen.")






