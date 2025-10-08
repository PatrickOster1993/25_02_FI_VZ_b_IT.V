# Konstanten
FAKTOR = 9.0 / 5.0
EXTRA = 32.0

# 1. Eingabe der Temperatur in Celsius
print("--- Temperaturkonvertierung: Celsius nach Fahrenheit ---")

#fragen und in float konvertieren, 
celsius_str = input("Geben Sie die Temperatur in Celsius (°C) ein: ")
temperatur_celsius = float(celsius_str)
30
# 2. Berechnung der Temperatur in Fahrenheit
# F = C * (9/5) + 32
temperatur_fahrenheit = temperatur_celsius * FAKTOR + EXTRA

# 3. Ausgabe der umgerechneten Temperatur
print("\n--- Ergebnis ---")

# Konvertierung der Float-Werte in String (Text) für die Ausgabe
print("Die eingegebene Temperatur betrug: " + str(temperatur_celsius) + " °C")
print("Umgerechnet in Fahrenheit (°F) ist das: " + str(temperatur_fahrenheit) + " °F")
print("----------------")