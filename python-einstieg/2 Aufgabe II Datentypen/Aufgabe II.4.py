# Aufgabe 4: Deklariere und initialisiere

# ----------------------------------------------------------------------
# 1. Das Ergebnis einer Addition von zwei int-Zahlen
# ----------------------------------------------------------------------

# Deklariere und initialisiere die zwei int-Zahlen
zahl_a = 15
zahl_b = 7

# Berechne die Addition und speichere das Ergebnis
ergebnis_addition = zahl_a + zahl_b

print(f"1. Addition: {zahl_a} + {zahl_b} = {ergebnis_addition}") 
# Ergebnis: 22


# ----------------------------------------------------------------------
# 2. Die Fläche eines Kreises mit einem gegebenen Radius (benutze float)
# Formel: Fläche = π * Radius²
# ----------------------------------------------------------------------

# Definiere die Konstante PI und den Radius als float
PI = 3.14159
radius = 5.0 # Als float initialisiert

# Berechne die Fläche
flaeche_kreis = PI * (radius ** 2)

print(f"2. Kreisfläche (Radius {radius}): {flaeche_kreis}") 
# Ergebnis: 78.53975


# ----------------------------------------------------------------------
# 3. Eine Nachricht, die zwei Strings miteinander kombiniert
# ----------------------------------------------------------------------

# Deklariere und initialisiere die zwei Strings
teil_1 = "Hallo, "
teil_2 = "wie geht es dir?"

# Kombiniere (konkateniere) die Strings
gesamte_nachricht = teil_1 + teil_2

print(f"3. Kombinierte Nachricht: {gesamte_nachricht}") 
# Ergebnis: Hallo, wie geht es dir?