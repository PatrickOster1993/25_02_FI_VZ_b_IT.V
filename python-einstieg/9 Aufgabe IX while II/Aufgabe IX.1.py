# Variablen
summe = 0.0          
anzahl_zahlen = 0    

# Erste Eingabe außerhalb der Schleife
print("--- DURCHSCHNITTSRECHNER ---")
print("Geben Sie positive Zahlen ein. Beenden Sie die Eingabe mit einer negativen Zahl.")
eingabe_str = input("Zahl eingeben: ")

#  Eingabe in eine Zahl umzuwandeln
aktuelle_zahl = float(eingabe_str)


# Die Schleife läuft, solange die aktuelle Zahl >= 0 ist (also positiv oder Null).
while aktuelle_zahl >= 0:
    
    # Die aktuelle Zahl zur Summe addieren
    summe = summe + aktuelle_zahl
    
    # Die Anzahl der Zahlen erhöhen
    anzahl_zahlen = anzahl_zahlen + 1
    
    # Neue Eingabe anfordern
    eingabe_str = input("Zahl eingeben: ")
    aktuelle_zahl = float(eingabe_str)


# Berechnung und Ausgabe des Durchschnitts, wenn Zahlen eingegeben wurden
print("\n--- ERGEBNIS ---")

# Prüfen, ob überhaupt positive Zahlen eingegeben wurden
if anzahl_zahlen > 0:
    # Berechnung des Durchschnitts
    durchschnitt = summe / anzahl_zahlen
    
    print(f"Es wurden {anzahl_zahlen} positive Zahlen eingegeben.")
    print(f"Gesamtsumme: {summe:.2f}")
    print(f"Der Durchschnitt beträgt: {durchschnitt:.2f}")

else:
    print("Es wurden keine positiven Zahlen eingegeben.")