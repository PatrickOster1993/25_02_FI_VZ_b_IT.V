Salat=False
mitFleisch=True
mitBrot=True
mitKaese=False

ganzenDöner=mitFleisch or (Salat and(mitBrot and mitKaese)) #wie Kette alles ist verbunden # in Klammern denken


print(ganzenDöner) # 3 /4 Der Ergebnisse beim UND Operator ergeben False

#beom ODER Operator wenn du eine Variable True ist, dann ist alles True 3/4 True


