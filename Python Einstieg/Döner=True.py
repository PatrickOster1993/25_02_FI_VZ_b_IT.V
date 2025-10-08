Döner=True
mitFleich=True
mitBrot=True

istkorekt=mitFleich and mitBrot #wie Kette alles ist verbunden mit and Operator

print(istkorekt) #3/4 Der Ergebnisse beim Und Operator ergeben FALSE 




Salat=False
mitFleich=True
mitBrot=False

ganzenDöner=mitFleich or Salat or mitBrot #wie Kette alles ist verbunden

#beim ODER Operator wenn du eine Variable True ist dann ist alles True 3/4 True
print(ganzenDöner)



Salat=False
mitFleich=True
mitBrot=False
mitKaese=False

ganzenDöner=mitFleich or Salat or mitBrot and mitKaese ==True
#

print(ganzenDöner)