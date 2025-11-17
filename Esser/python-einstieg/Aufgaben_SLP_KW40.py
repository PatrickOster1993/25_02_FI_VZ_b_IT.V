# Euro in Yen umrechnen
#Wechselkurs für 1€ = 175,5 Yen

betragineuro = float(input("Betrag in Euro:    "))
aktuellerwechselkurs = float(input("Wie ist der aktuelle Wechselkurs von € in Yen:   "))

betraginyen = betragineuro*aktuellerwechselkurs
print(f"    Sie erhalten genau {betraginyen:.2f} . Möhten Sie abheben?")

