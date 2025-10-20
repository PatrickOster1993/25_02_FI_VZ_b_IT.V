zimmerpreis=float(input("Bitte geben sie den Zimmerpreis ein"))
aufenthaltsdauer=int(input("Geben sie die Dauer des Aufenthaltes ein"))
alter_kind=int(input("Geben sie das Alter des Kindes ein"))



if alter_kind <7:
    rabatt=100
elif alter_kind >=18:
    rabatt=0
else:
    rabatt=70


kinderpreis=zimmerpreis*aufenthaltsdauer*(1- rabatt/100)
erwachsenenpreis= 2*zimmerpreis*aufenthaltsdauer
gesamtpreis=erwachsenenpreis+kinderpreis

print(f"Der Aufenthalt in unserem Hotel kostet für sie {gesamtpreis:.2f} €")