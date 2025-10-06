AnzahlPersonen=int(input("Anzahl der Personen: "))
Aufenthaltsdauer=int(input("Aufenthaltsdauer in Tagen: "))

Zimmerpreis=70
Nettopreis=Zimmerpreis*AnzahlPersonen*Aufenthaltsdauer
Gesamtpreis=Nettopreis*1.19

print(f"Der Gesamtpreis beträgt: {Gesamtpreis} Euro")

