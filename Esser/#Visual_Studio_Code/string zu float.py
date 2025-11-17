x = "123,32"
x_bereinigt = x.replace(',', '.')
try:
    float_wert = float(x_bereinigt)
    print(f"Wert als float: {float_wert}")
except ValueError:
    print("Falsche Eingabe")