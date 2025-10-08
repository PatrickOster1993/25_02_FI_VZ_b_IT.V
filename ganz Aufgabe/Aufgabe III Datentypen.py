
#Zinsberechnung
Gesamtbetrag=float(input("Gib dein betrag in Euro ein :  "))
zinssatz=float(input("Gib den zinssatz ein in % :  "))
Jahren =int(input("Gib die lauf zeit in die jahren : "))

zinssatzprojahr=Gesamtbetrag*(zinssatz/100)
Gesamtzinssatz= zinssatzprojahr*Jahren


print(f"zinssen pro jahr : {zinssatzprojahr} Euro")
print(f"Gesamtzinssatz : {Gesamtzinssatz} Euro")