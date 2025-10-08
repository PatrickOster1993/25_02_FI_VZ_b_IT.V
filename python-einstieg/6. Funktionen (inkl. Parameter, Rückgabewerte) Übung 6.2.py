# Definition der Funktion
def erstelle_begruessung(name):
    begruessungstext = "Willkommen, " + name + "!"
    return begruessungstext

# Testen der Funktion
print("\n--- Begrüßung mit Rückgabewert ---")
ausgabe_text = erstelle_begruessung("Max")
print(ausgabe_text)