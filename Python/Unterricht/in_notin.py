studenten = ["Jörg","Patrick","Erdal","Fabian","Dennis","Rüdiger","Christian","Holger"]

if "ErDaL".lower() in (student.lower() for student in studenten):
    print("Studiert")
else:
    print("Studiert nicht")

text = "Hi ich bin ein Berliner :)"

if ":)" in text:
    print("Hey der Smiley ist da")
else:
    print("Hey der Smiley ist nicht da")

zahl = 24
if "24" in str(zahl):
    print("Ja")
else:
    print("Nein")

if "PaTrIck".lower() not in (student.lower() for student in studenten):
    print("Patrick ist nicht dabei")
else:
    print("Patrick ist Dabei") 