import random
 
# Basisklasse = Krieger
class Krieger:                                                          # = Optional (kann, muss aber nicht zwingend!)
    def __init__(self, name, lebenspunkte, angriffskraft, verteidigung, ruestung = None):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.verteidigung = verteidigung
        self.setRuestung(ruestung)
 
    # "spezielle" Methode, die dem Interpreter mitteilt, wie das Objekt als "String-Kontext" zu handhaben ist!
    def __str__(self):
        return f"# {self.name} besitzt eine Angriffskraft von {self.angriffskraft}, eine Verteidigungsstärke i. H. v. {self.verteidigung} und verfügt aktuell über {self.lebenspunkte} Lebenspunkte!"
 
    def setRuestung(self, ruestung):
        if ruestung != None:
            self.verteidigung += ruestung.bonus
 
    def gegnerBesiegt(self, gegner):
        return gegner.lebenspunkte <= 0
 
    def angreifen(self, gegner):
            print(f"{self.name} greift {gegner.name} mit einer Angrifskraft von {self.angriffskraft} an!")
            schaden = self.angriffskraft - gegner.verteidigung
            if schaden <= 0:
                print(f"{self.name}`s Angriff zeigt keine Wirkung!")
            else:   
                gegner.lebenspunkte -= schaden
                if self.gegnerBesiegt(gegner):
                    print(f"{gegner.name} bekommt {schaden} Schaden!\n{gegner.name} wurde besigt!!")
                else:
                    print(f"{gegner.name} bekommt {schaden} Schaden!\nSeine Lebenspunkte fallen auf {gegner.lebenspunkte}!")
 
# Sub-Klasse = Paladin (= Krieger mit speziellen Add-ons / Optimierungen / Anpassungen, etc.)
class Paladin(Krieger):
    def __init__(self, name, lebenspunkte, angriffskraft, verteidigung, ruestung = None):
        super().__init__(name, lebenspunkte, angriffskraft, verteidigung, ruestung)
        self.angriffskraft = int(1.5 * self.angriffskraft)
        self.verteidigung = int(0.75 * self.verteidigung)
 
class Ruestung:
    def __init__(self, bezeichnung, bonus):
        self.bezeichnung = bezeichnung
        self.bonus = bonus
 
    def __str__(self):
        return f"{self.bezeichnung} liefert einen Verteidigungsbonus i. H. v. {self.bonus}"
 
# mein_krieger = Krieger("Hans", 90, 75, 40) # --> nicht empfohlen!
mein_krieger = Krieger( # --> empfohlen (erspart uns zukünftig den ein oder anderen Ärger, wen SW wächst!)
    angriffskraft = 75,
    lebenspunkte = 90,
    name = "Hans",
    verteidigung = 40,
    ruestung = Ruestung(
        bezeichnung="Geisteskranke Rüstung",
        bonus = 200
    )
)
 
mein_palladin = Paladin(
    angriffskraft = 75,
    lebenspunkte = 95,
    name = "Friedrich",
    verteidigung = 40,
    ruestung = Ruestung(
        bezeichnung="Magischer Schild",
        bonus = 25
    )
)
 
## Beziehung zwischen Rüstung und Krieger Aggregation oder Komposition???
### Es handelt sich um eine Aggregations-Beziehung11ELF
 
def kampfsimulation(krieger1, krieger2):
    # Simulation über den Verlauf und Ausgang des Kampfes zwischen krieger1 und krieger2
    while(True): # unendlich laufende while-Schleife, weil unklar, wie lange / wieviele Runden Kampf dauert!
        krieger = [krieger1, krieger2]
        angreifer_index = random.randint(0, 1) # zufällig entscheiden, ob Index 0 oder 1
        angreifer = krieger[angreifer_index]
        krieger.remove(angreifer)
        verteidiger = krieger[0]
        angreifer.angreifen(verteidiger)
        if angreifer.gegnerBesiegt(verteidiger):
            break
 
kampfsimulation(mein_krieger, mein_palladin)