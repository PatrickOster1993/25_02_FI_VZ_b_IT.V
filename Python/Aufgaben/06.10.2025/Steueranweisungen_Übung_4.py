#Übung 4.1 Rabattaktion

#Festlegung der Grundlegenden Variablen des Programms 
warenkorb_wert = float(input("Warenkorb Wert"))
rabbatt_schwelle = 50
rabatt_prozent = 0.1

#Abfrage für gewährleistung eines Rabatts und dessen Ausgabe
if warenkorb_wert > rabbatt_schwelle:
    zu_bezahlen = warenkorb_wert*(1-rabatt_prozent)
    print(f"Der zu zahlende Betrag lautet: {zu_bezahlen:.2f}€")
    print("Beehren Sie uns bald wieder")
else:
    print("Leider qualifizieren Sie sich nicht für unsere Rabattaktion")
    print(f"Der zu zahlende Betrag Lautet: {warenkorb_wert:.2f}€")
    print("Beehren Sie uns bald wieder")

#Übung 4.2 Notensystem

punkte = float(input("Punktzahl eintragen"))
if punkte >= 90:
    print("Note 1")
elif punkte >= 80:
    print("Note 2")
elif punkte >= 70:
    print("Note 3")
elif punkte >= 60:
    print("Note 4")
else:
    print("Note 5")

#Übung 4.3 7er Reihe

sieben_reihe = [7,14,21,28,35,42,49,56,63,70]
for zahl in sieben_reihe:
    print(zahl)

#Alternative

for b in range(0,70,7):
    print(b)
    