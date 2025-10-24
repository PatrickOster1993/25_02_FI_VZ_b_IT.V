#liste=[1,2,3,4,5,6,7,8,9,10]

#for zaehle in liste:
#    print(zaehle)



#Aufgabe 2

#liste=range(1,11)
#multiplikator = int(input(" geben sie eine Zahl ein:"))
#ergebnis=0
#for zahl in liste:
#    ergebnis=multiplikator*zahl
#    print(f"{multiplikator} x {zahl} = {ergebnis}")

#Aufgabe3

try:
    eingabe = float(input("Geben Sie eine Zahl ein, um sie zu quadrieren: "))
    quadrat_eingabe = eingabe ** 2
    print(f"Das Quadrat von {eingabe} ist {quadrat_eingabe:.2f}")
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")