class Dozent():
   def name(self):
       print(f"{self.firstname} {self.lastname}")


erdal=Dozent()#instanz und der vorgan Instanziierung
erdal.firstname= "Erdal"
erdal.lastname="Cakir"

print(erdal.firstname)
print(erdal.lastname)



mira=Dozent()
mira.firstname="Mira"
mira.lastname="Cakir"





class Auto():
    def name(auto):
        print(f"{auto.bezeichnung} {auto.typ}")

car=Auto()
car.bezeichnung="Audi"
car.typ="Sportwagen"

class Smartphone():
    def name(self):
        print(self.bezeichnung+ " "+ self.typ)

handy= Smartphone()
handy.bezeichnung= "Samsung Galaxy S10"
handy.typ= "Smartphone"
handy.name()

def namexmal(x):
    x.name()
    x.name()
    x.name()
namexmal(mira)
namexmal(handy)
namexmal(erdal)
