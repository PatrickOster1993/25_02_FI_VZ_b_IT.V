a=2
print("Die Zahl 2 ist ein ",type(a)) #int

b=13//6
print("Die Zahl 13//6 ist ein ",type(b))   #int

b=12/6
print("Die Zahl 12/6 ist ein ",type(b))   #float

c="123"
print("Die Zahl '123' ist ein ",type(c))   #str

x=12
print("x",x)
print("x==12:",x==12) #True Bool
print(type(x==12)) #bool

x=12
print("x",x)
print("==12:",(x!=12)) #False Bool
print(type(x!=12)) #bool


eingabe=int(input("Trage zunächst die erste Zahl ein: "))
eingabe2=int(input("Trage jetzt die zweite Zahl ein: "))
ergebnis=eingabe*eingabe2
print(f"Das Ergebnis ist: {ergebnis}")
print("Datentyp des Ergebnisses lautet",type(ergebnis)) #int

