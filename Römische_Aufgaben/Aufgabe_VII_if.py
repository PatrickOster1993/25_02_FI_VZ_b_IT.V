Zimmerpreis = float(input("Wie teuer ist das Zimmer? "))
Erwachsene = int(input("Wie viele Erwachsene (über 18 Jahre) kommen mit? "))
Kinder = int(input("Wie viele Kinder kommen mit (0-18 Jahre)? "))
aufenthalt = int(input("Wie viele Nächte möchten Sie bleiben? "))

rabatt_pro_kind = []
Kinderpreise = []


if Kinder == 1:
    AlterKind = int(input("Wie alt ist Ihr Kind? "))
    if AlterKind < 7:
        rabatt = 100
    else:
        rabatt = 70
    rabatt_pro_kind.append(rabatt)
    preis = Zimmerpreis * aufenthalt * (1 - rabatt/100)
    Kinderpreise.append(preis)
        
elif Kinder>1:  #Rabatte bei mehr als einem Kind

    for i in range(Kinder):
        alter = int(input(f"Wie alt ist Kind {i+1}? "))
        if alter < 7:
                rabatt = 100
        else:
                rabatt = 70
    rabatt_pro_kind.append(rabatt)
    preis = Zimmerpreis * aufenthalt * (1 - rabatt/100)
    Kinderpreise.append(preis)
    
    
    
    
else:       #Rabatt ohne Kinder
    rabatt_pro_kind = []


Erwachsenenpreis = Erwachsene * Zimmerpreis * aufenthalt
Gesamtpreis = Erwachsenenpreis + sum(Kinderpreise)

print(f"Der Gesamtpreis für Ihren Aufenthalt beträgt: {Gesamtpreis:.2f} Euro.")
#Dies ist ein Test um mir mein Hirn kaputt zu machen