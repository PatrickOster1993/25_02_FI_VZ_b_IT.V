#Listen heißen auch Arrays
umschueler=[45,76,23,1] #Ohne Klammern ist es ein Tupel
print(type(umschueler))

umschueler.append (40) #append Hinzufügen 
print(umschueler)

umschueler.remove(umschueler[3]) #remove Entfernen der definierten eingabe 
print(umschueler)

geld=umschueler[2]
print(geld)

liste=len(umschueler) #len zählt die anzahl der Elemente in der Liste
print(liste) 

umschueler.pop(2) #pop Entfernen eines eingegebenen Indexes Default last
print(umschueler)