#Übung 6.1
def addition(a,b):
    summe = a+b
    return summe

print(addition(12,32))

#Übung 6.2
def beruessen(name):
    hallo = f"Hallo {name}\nWillkommen bei uns"
    return hallo

print(beruessen("Münster"))

#Übung 6.3
def flaeschen_berechnung(laenge,breite):
    """Berechnung einer Rechteckigen Flaesche mit laenge und breite"""
    flaesche = laenge*breite
    return flaesche

print(f"{flaeschen_berechnung(3,3)}cm²")
