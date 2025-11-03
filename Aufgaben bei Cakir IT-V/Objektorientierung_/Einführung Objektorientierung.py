class Dozent():
    pass# das heißt dass es ok ist wenn in der runden klammer nichts steht, sonst kommt ein fehler.

def get_name(Dozent):
    print(Dozent.firstname+" "+Dozent.lastname)


erdal=Dozent()#instanz und der vorgan Instanziierung
erdal.firstname= "Erdal"
erdal.lastname="Cakir"

print(erdal.firstname)
print(erdal.lastname)


get_name(erdal)
mira=Dozent()
mira.firstname="Mira"
mira.lastname="Cakir"

print(mira.firstname)
print(mira.lastname)

get_name(mira)