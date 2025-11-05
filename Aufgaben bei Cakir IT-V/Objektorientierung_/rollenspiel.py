import random
import time
class Krieger:
    def __init__ (self, name, hitpoints, schwäche):
        self.name=name
        self.hitpoints=hitpoints
        self.schwäche=schwäche
    def info(self):
        print("Krieger: ", self.name)
        print("Lebenspunkte: ", self.hitpoints)
        print("Schwäche: ", self.schwäche)
        print("--------------------------")
    def kämpfen(self):
        if self.hitpoints>50:
            print(self.name +"Kämpft noch locker weiter easy peasy ")
        else:
            print(self.name + "no easy peasy ist zu schwach, ich muss mich zurück ziehen und muss einen Döner zum Stärken Essen")
class Gladiator(Krieger):
    def __init__(self, name, hitpoints, schwäche, rüstung):
        super().__init__(name, hitpoints, schwäche)
        self.rüstung=rüstung
    def kämpfen(self):
        if self.hitpoints>70:
            print(self.name +" Nutzt seine Gladiatorfähigkeit " +self.rüstung+ "und Lebenspunkte steigen!")
        else:
            print(self.name +" verliert trotz  "+ self.rüstung+ " !!!!!! ")

class Jäger:
    def __init__(self, name, hitpoints, schwäche):
        self.name=name
        self.hitpoints=hitpoints
        self.schwäche=schwäche
    def jagen(self):
        if self.hitpoints>40:
            print(self.name+ "schleicht sich an die Beute ran und will mit seinem Bogen schiessen")
        else:
            print(self.name+ "ist zu schwach zum Angreifen und zieht sich zurück")

class spion(Jäger):
    def __init__(self, name, hitpoints, schwäche, tarnung):
        super().__init__(name, hitpoints, schwäche)
        self.tarnung=tarnung
    def jagen(self):
        if self.hitpoints>30:
            print(self.name+ " nutzt seine Tarnung (" + self.tarnung + ") und beobachtet den Feind")
        else:
            print(self.name+ " ist zu schwach seine Tarnung zu nutzen und wird erwischt")

class Assassine:
    def __init__(self, name, hitpoints, schwäche):
        self.name=name
        self.hitpoints=hitpoints
        self.schwäche=schwäche
    def anschleichen(self):
        if self.hitpoints>30:
            print(self.name+ " anschleichen ist noch möglich")
        else:
            print(self.name+ " Das Anschleichen ist nicht mehr möglich er ist zu laut und wird erwicht")                    

class Mörder(Assassine):
    def __init__(self, name, hitpoints, schwäche, waffe):
        super().__init__(name, hitpoints, schwäche)
        self.waffe=waffe
    def anschleichern(self):
        if self.hitpoints>30:
            print(self.name+ " erkann seine Waffe ("+self.waffe+") nutzen um den Feind zu besiegen")
        else:
            print(self.name+ " Er ist zu schwach und kann den Gegner nicht besiegen")



Kasper=Gladiator("Kasper", 80, "Feuer", "Stahlpanzer" )
Anselm=spion("Anselm", 35, "Gift", "Unsichtbarkeitsmantel")
Erdal=Mörder("Erdal", 65, "Lärm", "Dolch")

charaktere=[Kasper, Anselm, Erdal]

zufallschar=random.choice(charaktere)


for i in range(5):
    zufallschar=random.choice(charaktere)
    zufallschar.hitpoints=random.randint(10,100)


    print("Neue Lebenspunkte:", zufallschar.hitpoints) 

    if isinstance(zufallschar, Gladiator):
        zufallschar.info()
        zufallschar.kämpfen()
    elif isinstance(zufallschar, spion):
        zufallschar.jagen()
    elif isinstance(zufallschar, Mörder):
        zufallschar.anschleichen()

    time.sleep(2)
