zimmerpreis=float(input("Geben sie den Zimmerpreis für eine Person und Nacht an"))
aufenthaltsdauer= int(input("Geben sie die Aufenthaltsdauer in Nächten ein: "))
alter_kind=int(input("Geben sie jetzt das Alter des Kindes ein"))

if alter_kind <7: 
    rabatt=100 #rabatt für kinder 100%
elif alter_kind <18:#rabatt für Jugendliche 70%
    rabatt=70
else:
    rabatt=1 #rabatt für erwachsene keine

kinderpreis=zimmerpreis*aufenthaltsdauer*(1-rabatt/100)
erwachsenenpreis=2*zimmerpreis*aufenthaltsdauer
gesamtpreis=kinderpreis+erwachsenenpreis

print(f" Der Aufenthalt in unserem Luxushotel beträgt für dies Familie {gesamtpreis}")
