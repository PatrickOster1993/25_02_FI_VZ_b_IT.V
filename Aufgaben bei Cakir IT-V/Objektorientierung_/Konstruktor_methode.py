class Dozent():
    def __init__(self, firstname, lastname):
        self.firstname= firstname
        self.lastname= lastname
        self.grade=1

    def name(self):
        print(self.firstname+ " "+ self.lastname+ " (Note:  "+str(self.grade)+ ")")
erdal=Dozent("Erdal", "Cakir")
erdal.name()

mira=Dozent("Mira", "Cakir")
mira.name()