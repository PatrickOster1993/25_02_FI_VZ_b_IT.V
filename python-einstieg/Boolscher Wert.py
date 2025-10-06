Montag = True #entwerder True oder False
a = 3
b = 3
c= a == b
print(c)
print("")
Salat = True
mitFleisch = True
mitBrot = True

Komplett = Salat and mitBrot and mitFleisch

print(Komplett)
print("")
Salat = True
mitFleisch = False
mitBrot = True

Komplett = Salat or mitBrot or mitFleisch
print(Komplett)
print("")
Salat = True
mitFleisch = False
mitBrot = True
mitKaese = False
Komplett = Salat or mitBrot or mitFleisch and mitKaese
print(Komplett)
print("")
komplett = Salat and mitFleisch or mitBrot and mitKaese
print(komplett)
