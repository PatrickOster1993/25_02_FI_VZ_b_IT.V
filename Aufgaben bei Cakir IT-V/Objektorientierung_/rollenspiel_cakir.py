import random
import time 

#basic class Krieger

class Krieger():
    def __init__(self, name, hitpoints, schwäche):#konstruktor methode
        self.name=name#..objektvariable für name
        self.hitpoints=hitpoints #objektvariable für Lebenspunkte
        self.schwäche=schwäche#objektvariable für schwäche des Kriegers
    
    def info(self): #Methode zur Charakteinfo
        print("Krieger: ", self.name)
        print("Lebenspunkte: ", self.hitpoints)
        print("Schwäche: ",self.schwäche)
        print("--------------------------")

    def kämpfen(self):#Methode welche das Verhalten beim Kämpfen beschreibt
        if self.hitpoints>50: #wenn meine Lebenspunkte über 50
            print(self.name +" kämpft noch locker weiter easy peasy ") #also ist unser Krieger happy im Sinne happy wife happy life
        else:
            print(self.name + " no easy peasy ist zu schwach ich muss mich zurückziehen")

class Gladiator(Krieger):#Gladiator erbt vom Kriegerchen
    def __init__(self, name, hitpoints, schwäche, rüstung):#bitte Gladiator Directors cut schauen heute aber hier zusätzlicher Parameter Rüstung
        super().__init__(name, hitpoints, schwäche)#ruft lediglich den Konstruktor der Elternklasse auf (krieger)
        self.rüstung=rüstung #neue Objektvariable der Klasse Gladiator

    def kämpfen(self): #überschreibt oder auch ersetzt die kämpfen() Methode aus Krieger
        if self.hitpoints>70:
            print(self.name+ " nutze seine Gladiatorfähigkeit" + self.rüstung+ " und Lebenspunkte steigt und er siegt!")
        else:
            print(self.name+ " verliert den Kampf trotz "+ self.rüstung+ " !!!!!!")

class Jäger:
    def __init__(self, name, hitpoints, schwäche):
        self.name=name
        self.hitpoints=hitpoints
        self.schwäche=schwäche
    def jagen(self):#verhalten des jäger
        if self.hitpoints>40:
            print(self.name+ " schleicht sich an Beute ran und will mit dem Bogen schießen...")
        else:
            print(self.name+" ist zu stark verletzt um Beute zu jagen und geht nach Hause...")

class Spion(Jäger):
    def __init__(self, name, hitpoints, schwäche, tarnung):
        super().__init__(name, hitpoints, schwäche)
        self.tarnung=tarnung
    def jagen(self):#überschreibung der Elternklasse
        if self.hitpoints>30:
            print(self.name+ " nutzt seine SuperDuperTarnung (" + self.tarnung+ ") und beobachtet den Feind")
        else:
            print(self.name+" wurde erwischt oh nein und flieht....")

class Assassine:
    def _init_(self,name, hitpoints,schwäche):
        self.name=name
        self.hitpoints=hitpoints
        self.schwäche=schwäche

    def anschleichen(self):
        if self.hitpoints>50:
            print(self.name + " bewegt sich lautlos im Schatten und campt um seine Gegner so Feige wie er isst abzustechen")
        else:
            print(self.name+ " stolpert und denkt sich fuck ich mache zu viele Geräusche erstmal muss ich wo anders Frust rauslassen")

class Mörder(Assassine):
    def __init__(self, name, hitpoints, schwäche, waffe):
        super()._init_(name, hitpoints, schwäche)
        self.waffe=waffe
    def anschleichen(self):
        if self.hitpoints>60:
            print(self.name+ " greift diesmal mit seiner Waffe an "+self.waffe+ " und verletzt als Mörder tödlich den Gegner....")
        else:
            print(self.name+ " verfehlt sein Ziel, weil er geschwächt ist oh Mann ich muss mich erstmal erholen..")
            
#Objekt aka Instanzen

Kasper=Gladiator("Kasper",80, "Feuer", "Stahlpanzer")#Objekt für Gladiator
Anselm= Spion("Anselm", 35, "Gift", "Unsichtbarkeitsmangel")
Erdal= Mörder("Erdal",65, "Lärm", "Dolch")

charaktere= [Kasper, Anselm, Erdal]# Liste erstellt von verschiedenen Objekten aus unterschiedlichen Klassen

zufallschar=random.choice(charaktere)
#überprüfe doch den typ des charakters und führe eine entprechende Methode aus

for i in range(5):
    zufallschar=random.choice(charaktere)
    zufallschar.hitpoints=random.randint(10,100)
    

    print("Neue Lebenspunkte :", zufallschar.hitpoints)

    if isinstance(zufallschar, Gladiator):# in dem Fall wenn Gladiator gewählt wurde
        zufallschar.info()
        zufallschar.kämpfen()

    elif isinstance(zufallschar,Spion):
        zufallschar.jagen

    elif isinstance(zufallschar,Mörder):
        zufallschar.anschleichen()
    time.sleep(2)



        

        
        
 