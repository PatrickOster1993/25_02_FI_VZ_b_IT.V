# Übung 6.1: Additions-Funktion
def addiere(a,b):
    return a + b

ergebnis = addiere (7,5) 

print (f"das ergebnis ist : {ergebnis}") 

#	Übung 6.2: Begrüßung mit Rückgabewert
def erstelle_begruessung(name):
    print( f"Hallo,{name}")
   
    erstelle_begruessung("ehssan")

#	Übung 6.3: Flächenberechnung als Funktion

def berechne_rechteck_flaeche(laenge, breite):
    return(laenge*breite)

ergebnis_fläche= berechne_rechteck_flaeche(3, 4)

print(f"die ergebnis der fläche ist : {ergebnis_fläche}")


#1. Schreiben Sie eine Funktion namens drucke_produkt_info.

lage=[]

lage.append({"name":"Mausx",
      "produkt_id":548625,
      "lagerbestand":3,
})
lage.append({"name":"CD",
      "produkt_id":47897,
      "lagerbestand":5,
})
lage.append({"name":"HDD 1 TB",
      "produkt_id":548625,
      "lagerbestand":4,
})
for Produkt in lage : 
      
      print (f"ID : {Produkt['produkt_id']} , name : {Produkt['name']} , Lagerbestand: {Produkt['lagerbestand']}")
      
def drucke_produkt_info(Produkt):
    print (f"ID : {Produkt['produkt_id']}")
drucke_produkt_info (lage[1])
   
def berechne_gesamtlagerwert(list):
    gesamtwert=int(0)
    for list in lage:
     gesamtwert=list['lagerbestand']*75   
    return gesamtwert # warum ohne return die ergneise none
gesamt_preis=berechne_gesamtlagerwert(list)    
print (gesamt_preis)





