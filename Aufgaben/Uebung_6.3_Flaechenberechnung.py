# 6.3: Flaechenberechnung als Funktion

def berechne_rechteck_flaeche(laenge,breite):
    """Berechnet eine Fläche"""
    flaeche = laenge*breite
    return flaeche

laenge = float(input("\nHier Länge in cm angeben: "))
breite = float(input("\nHier Breite in cm angeben: "))

ergebnis = berechne_rechteck_flaeche(laenge,breite)

print(f"\nDas Ergebnis lautet: {ergebnis:.2f} cm^2")
print("")
