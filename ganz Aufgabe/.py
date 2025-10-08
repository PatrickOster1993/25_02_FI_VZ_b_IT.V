zimmerpreis=float(input("Geben sie den zimmerpreis für ein person und nacht ein "))
aufenthaltsdauer = int(input("Geben sie Die Aufenthaltsdaue in Nächten ein : "))
alter_kind=int(input("Geben Sie jetzt bitte das allter des kind : "))


if alter_kind <7:
    rabatt=100
elif alter_kind <18:
    rabatt= 70    
else:
    rabatt=0
    
kinderpreis=zimmerpreis*aufenthaltsdauer*(1-rabatt/100) 
erwachsenpreis=2*zimmerpreis*aufenthaltsdauer
gesamtpreis=kinderpreis+erwachsenpreis

print(f"Der Aufenthalt in unserem horel beträgt fir diese Familie {gesamtpreis}")
       