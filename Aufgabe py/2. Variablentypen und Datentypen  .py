programm_name =str(input( "was Namen des Produkts : " ))
Nettopreis =float(input("Geben Sie Den Nettopreis an : "  ))
Stückzahl =int(input("Geben Sie die gewünschte Stückzahl : "  ))
Mehrwertsteuer = float (0.19)

Den_Gesamt_Nettopreis = (Nettopreis *Stückzahl )
Die_anfallende_Mehrwertsteuer= (Den_Gesamt_Nettopreis *Mehrwertsteuer ) 
Den_Gesamt_Bruttopreis= (Den_Gesamt_Nettopreis+Die_anfallende_Mehrwertsteuer)

print (f"Gesamt-Nettopreis: {Den_Gesamt_Nettopreis} Euro ")

print (f"+ 19% mwSt : {Die_anfallende_Mehrwertsteuer} Euro ")

print (f"Gesamt-Bruttopreis: {Den_Gesamt_Bruttopreis} Euro ")
