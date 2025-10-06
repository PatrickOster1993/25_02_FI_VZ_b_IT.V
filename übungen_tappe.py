#Übung 4.1: Rabattaktion

warenkorb_wert = float(input("Geben Sie den Warenkorbwert ein: "))

if warenkorb_wert > 50.00:
    rabatt = warenkorb_wert * 0.10
    neuer_preis = warenkorb_wert - rabatt
    print("Rabatt erhalten! Neuer Preis: ", round(neuer_preis, 2), "Euro")
else:
    print("Leider kein Rabatt")

#Übung 4.2: Notensystem

punktzahl = int(input("Geben Sie die erreichte Punktzahl (0-100) ein: "))

if punktzahl >= 90:
    print("Note 1")
elif punktzahl >= 80:
    print("Note 2")
elif punktzahl >= 70:
    print("Note 3")
elif punktzahl >= 60:
    print("Note 4")
else:
    print("Note 5")

#Übung 4.3: Die 7er-Reihe

for i in range(7, 71, 7):
    print(i)

#Übung 5.1: Einkaufsliste

einkaufsliste = ["Milch", "Brot", "Eier"]
print(einkaufsliste[1])
einkaufsliste.append("Butter")
einkaufsliste[0] = "Hafermilch"
print(einkaufsliste)

#Übung 5.2: Benutzerprofil
#----

#Übung 6.1: Additions-Funktion

def addiere(a, b):
    return a + b

ergebnis = addiere(5, 7)
print(ergebnis)

#Übung 6.2: Begrüßung mit Rückgabewert

def erstelle_begruessung(name):
    return "Willkommen, " + name 

text = erstelle_begruessung("Tappe")
print(text)

#Übung 6.3: Flächenberechnung als Funktion

def berechne_rechteck_flaeche(laenge, breite):
    return laenge * breite

flaeche = berechne_rechteck_flaeche(5, 3)
print("Die Fläche beträgt:", flaeche)
