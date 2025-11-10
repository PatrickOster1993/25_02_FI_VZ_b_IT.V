# Fehlerhaftes Programm, das den TypeError erzeugt
meine_zahl = 100
meine_zeichenkette = "200"

# Versuch, eine Zahl von einer Zeichenkette zu subtrahieren
# Das führt zum Fehler: TypeError: unsupported operand type(s) for -: 'str' and 'int'
ergebnis = meine_zeichenkette - meine_zahl

print(ergebnis)