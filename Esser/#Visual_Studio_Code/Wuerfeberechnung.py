a = "10"
b = "19.3"
V = "a*a*a"
m = "d*v"
print ("Würfel mit der Seitenlänge",a,"cm")
print ("Masse:",m,"g")

print ("Berechnung der Masse einesWürfels")
print("==================================")
a = input ("Kantenlänge [cm]:")
a = int (a)
mat = input("Material:")
d = input("Materialdichte [g/cm3]:")
d = float(d)
V = a*a*a       # Volumen
m = d*V         # Masse
print ("berechnete Masse:",m,"g",mat)
if a>0 and d>0:
    V = a*a*a   #Volumen
    m = d*V
    print ("berechnete Masse:",m,"g",mat)
else:
    print ("ungültige Werte.")