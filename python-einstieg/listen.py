schueler0 = "Möller"
schueler1 = "Ohletz"
schueler2 = "Noory"
schueler3 = "Goebel"

umschueler = ["Moeller", "Ohletz", "Noory", "Goebel"]

#Listen sind veränderbar
print(umschueler)
print("")
print(len(umschueler))
umschueler.append("Esser")  #Der LISTE wird etwas hinzugefügt 
print(umschueler)
print(len(umschueler))

print("")
print(umschueler[3])
print("")
umschueler.pop()
print(umschueler)
umschueler.pop()
print(umschueler)
umschueler.pop(0)
print(umschueler)
print("")
umschueler.remove('Ohletz')
print(umschueler)
print("")

("Bei den Umschülern handelt es sich um ", type(umschueler))
print("")
schueler0 = "Möller"
schueler1 = "Ohletz"
schueler2 = "Noory"
schueler3 = "Goebel"

umschueler = "Moeller", "Ohletz", "Noory", "Goebel"

#Tuple sind UN-veränderbar

print(umschueler)
print("")
print("Bei den Umschülern handelt es sich um ", type(umschueler))




