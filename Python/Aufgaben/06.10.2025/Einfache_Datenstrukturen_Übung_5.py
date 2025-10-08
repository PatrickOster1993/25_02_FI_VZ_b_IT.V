#Übung 5.1 Einkaufsliste
einkaufliste = ["Wein","Speck","Pommes"]
print(einkaufliste[1])
einkaufliste.append("Butter")
einkaufliste.pop(0)
einkaufliste.insert(0,"Hafermilch")
print(einkaufliste)

#Übung 5.2 Benutzerprofil
benutzerprofil = {"Vorname":"Max","Nachname":"Mustermann","Alter":32,"Stadt":"Musterhausen"}
print(benutzerprofil["Nachname"])
benutzerprofil["Alter"] = 18
benutzerprofil["E-Mail"] = "max.mustermann@webmailer.de"
print(benutzerprofil)

#Aufgabe Lagerverwaltung 

produkt1 = {"ID":2110,"Name":"SSD 1TB","Bestand":10}
produkt2 = {"ID":2111,"Name":"SSD 2TB","Bestand":5}
produkt3 = {"ID":2010,"Name":"HDD 500GB","Bestand":21}
lager = [produkt1,produkt2,produkt3]
for a in lager:
    gesamter_warenwert = a["Bestand"]*50
    print(f"Produkt: {a["Name"]}, aktueller Bestand: {a["Bestand"]} Stück, Gesamtwert: {gesamter_warenwert}€")
