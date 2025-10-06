Warenkorbwert = int(input("Wie hoch sind die Gesamtkosten?    "))

if Warenkorbwert > 50:
        print(f"Ihr Warenkorb erhält einen Rabatt ihr Gesamtpreis ist {Warenkorbwert-Warenkorbwert*0.1}")
        
else:
        print(f"Leider erhalten sie keinen Rabatt. Ihr Gesamtpreis ist {Warenkorbwert}.")
        
        

#Übung 4.2

punktzahl=int(input("Gebe deine Anzahl der Punkte vom Test ein von 1-100"))

if punktzahl >90:
    print("Sehr gut.")
elif punktzahl > 80:
    print("Gut.")
elif punktzahl > 70:
    print("Befriedigend.")
elif punktzahl > 60:
    print("Ausreichend.")
else:
    print("Nächstes mal vielleicht...")
    
#Übung 4.3

for i in range(7,71,7):
    print(i)