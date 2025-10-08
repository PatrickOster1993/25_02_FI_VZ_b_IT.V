# Definition der Funktion
def berechne_rechteck_flaeche(laenge, breite):
    """
    # Berechnet die Fläche eines Rechtecks aus der gegebenen Länge und Breite.
    Gibt die berechnete Fläche als Zahl zurück.
    """
    flaeche = laenge * breite
    return flaeche # Gibt die berechnete Fläche zurück

# Testen der Funktion
laenge_wert = 12
breite_wert = 5
flaeche_ergebnis = berechne_rechteck_flaeche(laenge_wert, breite_wert)

print("\n--- Flächenberechnung ---")
print(f"Rechteck mit Länge {laenge_wert} und Breite {breite_wert}.")
print(f"Die berechnete Fläche beträgt: {flaeche_ergebnis}")