#1. Erstellen Sie eine Liste namens lager.
lage=[]
#Dictionary

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
#chreiben Sie eine for-Schleife, die durch Ihre lager-Liste iteriert
for Produkt in lage : 
      
      print (f"ID : {Produkt['produkt_id']} , name : {Produkt['name']} , Lagerbestand: {Produkt['lagerbestand']}")
#Innerhalb der Schleife: Geben Sie für jedes Produkt einen Satz aus, der den Namen und den aktuellen Lagerbestand enthält

for produkt in lage :

 print (f"produkt name : {Produkt['name']} ,Aktueller Bestand : {Produkt['lagerbestand']} ")
 
 #Optional) Erstellen Sie eine Variable gesamter_warenwert. Nehmen Sie an, jedes Produkt kostet 50
 gesamter_warenwert=Produkt['lagerbestand']*50
 
 print(f"Aktueller Bestand : {gesamter_warenwert} ")
 