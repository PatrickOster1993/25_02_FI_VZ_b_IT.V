Lager=[]

for i in range(3):
    print(f"Artikel {i+1}")
    
    produkt_id=input("Wie ist die Produkt_ID")
    Name=input("Wie lautet der Name des Produts?")
    Lagerbestand=int(input("Wieviel haben wir noch?"))
    
    Produkt= {"produkt_id": produkt_id, "Name": Name, "lagerbestand": Lagerbestand, }
    
    Lager.append(Produkt)
    
print(Lager)