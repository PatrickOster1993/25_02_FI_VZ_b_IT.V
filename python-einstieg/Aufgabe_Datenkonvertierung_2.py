# Aufgaben zur Datenonvertierung - Aufgabe 2
print("") 
# Euro in US-Dollar umrechnen   #   #Wechselkurs für 1€ = 1,1 US-Dollar

Eurobetrag = str(input("Betrag in Euro:    "))
Wechselkurs = str(input("Wie ist der aktuelle Wechselkurs von € in US-Dollar:   "))
Eurobetrag_korrekt = Eurobetrag.replace(",",".")
try:
    float_wert_betrag = float(Eurobetrag_korrekt)
    print(f"Der angegebene Betrag lautet:    {Eurobetrag_korrekt} €")
except ValueError:
    print("Die Eingabe war Fehlerhaft")
Wechselkurs_korrekt = Wechselkurs.replace(",",".")
try:
    float_wert_wechsel = float(Wechselkurs_korrekt)
    print(f"Der Wechselkurs wurde mit:  {Wechselkurs_korrekt}   angegeben")
except ValueError:
    print("Die Eingabe war Fehlerhaft")
US_Dollarbetrag = float(float_wert_betrag*float_wert_wechsel)  
if Eurobetrag_korrekt==float or int and Wechselkurs_korrekt==float or int:
    print(f"    Sie erhalten genau {US_Dollarbetrag:.2f} $. ")
    Abhebung = (input("Give the Money? Y/N  " ))
    if Abhebung == "Y" or Abhebung == "y":
        print("Eine gute Wahl, aber geben Sie nicht alles auf einmal aus")
    if Abhebung == "N" or Abhebung == "n":
        ganzssicher = input("Es ist immer gut, etwas zu sparen.  Wollen Sie einen anderen Betrag abheben? Y/N    "   )
        if ganzssicher =="Y" or ganzssicher == "y":
            Abhebung_neu = str(input("Ausgezeichnet, geben Sie den Betrag nun ein:  "   ))     
            Abhebung_neu_korrekt = Abhebung_neu.replace(",",".")
            try:
                float_wert_betrag_neu = float(Abhebung_neu_korrekt)
                print(f"Der neue Betrag wurde mit: {Abhebung_neu_korrekt}€ angegeben.") 
            except ValueError:
                print("Die Eingabe war Fehlerhaft") 
            US_Dollarbetrag_neu = float(float_wert_betrag_neu*float_wert_wechsel)
            print(f" Das ergibt bei einem Umrechnungsfaktor von: {Wechselkurs_korrekt} , einen Betrag von: {US_Dollarbetrag_neu:.2f} US-Dollar. ") 
            print("Der Betrag wird Ihnen nun ausgezahlt - bitte prüfen Sie das Geldausgabefach.")
        if ganzssicher == "N" or ganzssicher =="n":
            print("Na gut, dann bleibt das Geld hier und wir zocken ein bisschen damit")
        else: 
            print("Bitte überprüfen Sie Ihre Angaben")
else:
    print("WTF")


