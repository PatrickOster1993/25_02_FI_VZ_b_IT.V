Zimmerpreis=70
personen=int (input ("Mit wievielen Personen wollen sie einchecken"))
aufenthaltsdauer=int (input ("Wie lange wollen sie in unserem Hotel übernachten"))
mwst=1.19
nettopreis=(Zimmerpreis*personen*aufenthaltsdauer)
gesamtpreis=nettopreis*mwst
aufschlag=20
aufschlagspreis=gesamtpreis+aufschlag

if aufenthaltsdauer==1:
    print(f"Sie müssen einen Aufschlag von {aufschlag} € bezahlen")
    print(f"Ihr betrag lautet {aufschlagspreis} €")
else:
    print(f"Sie müssen {gesamtpreis:.2f} € bezahlen")

