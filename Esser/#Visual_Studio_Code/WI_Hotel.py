zimmerpreis = float (input("Geben Sie den Zimmerpreis für eine Person und Nacht ein: "))
aufenthaltsdauer = int(input("Geben Sie die Aufenthaltsdauer in nÄchten ein: "))
alter_kind = int(input("Geben Sie bitte das Alter des Kindes ein: "))

if alter_kind <7:
    rabatt = 100
elif alter_kind <18:
    rabatt = 70
else: 
    rabatt = 0
    

Kinderpreis = zimmerpreis*aufenthaltsdauer*(1-rabatt/100)

Erwachsenenpreis = 2*zimmerpreis*aufenthaltsdauer

Gesamtpreis = Kinderpreis+Erwachsenenpreis

print(f"Der Aufenthalt in unserem Luxushotel beträgt für diese Familie {Gesamtpreis} € ")