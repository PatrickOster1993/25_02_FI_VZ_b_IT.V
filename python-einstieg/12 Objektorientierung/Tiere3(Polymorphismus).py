




### gleiche Schnittstelle
### vereinfacht gesagt
### aber führen diesen unterschiedlich aus (je nach Objekt)

##  Konstruktor: hilft,  die "initialen" Eigenschaften (=Attribute)
### eines Objektes der jeweiligen Klasse festzulegen

class Tier():
    def __init__(self, name):
        self.name = name
    def geraeusch(self): # Methode
        print(f"{self.name} gibt laut von sich!")

class Katze(Tier):
    def geraeusch(self):
        print(f"{self.name} miaut!")

class Hund(Tier):
    def geraeusch(self):
        print(f"{self.name} bellt!")

# Polymorhpismus ( = Schnittstelle)
def mach_geraeusch(tier: Tier):
    pass

mein_tier = Tier(name ="Lars")
# mein_tier.geraeusch()

dein_tier = Tier(name = "Sven")
# dein_tier.geraeusch()

katze = Katze(name = "Mieze")
# katze.geraeusch()

hund = Hund(name = "Wauwau")
# hund.geraeusch()

mach_geraeusch(mein_tier)
mach_geraeusch(dein_tier)
mach_geraeusch(katze)
mach_geraeusch(hund)
