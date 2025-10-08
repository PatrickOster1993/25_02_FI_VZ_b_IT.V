Zimmerpreis=float(input("Wie teuer ist das Zimmer?"))
Kinder=int(input("Wieviele Kinder kommen mit (Alter 0-18 Jahre?  "))
Erwachsene=int(input("Wieviele Erwachsene (über 18 Jahren) kommen mit?"))
KinderListe=[]
rabatt_pro_kind = []  # Liste für individuellen Rabatt je Kind

if Kinder == int(1):
    AlterKind=int(input("Wie alt ist ihr Kind?"))
    if AlterKind > 7:
        rabatt= 100
    else:
        rabatt=70
        
elif Kinder>1:

    for i in range(Kinder):
        alter=int(input(f"Wie alt ist Kind {i+1}?"))
        KinderListe.append(alter)
    
        rabatt = 0
        for alter in KinderListe:
            if alter > 7:
                rabatt = 100
            else:
                rabatt = 70
                
    rabatt_pro_kind.append(rabatt)   
    
    
else:
    rabatt_pro_kind = []


Gesamtpreis = (Zimmerpreis *Erwachsene) + (Zimmerpreis*Kinder) * (1 - rabattgesammt/100)
print(Gesamtpreis)


#Dies ist ein Test um mir mein Hirn kaputt zu machen