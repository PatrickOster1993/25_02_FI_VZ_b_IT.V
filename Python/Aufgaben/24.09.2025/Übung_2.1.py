#2.2
string="Hallo"
integer=233
float=3.141
boolean=True
print(type(boolean))
print(type(float))
print(type(integer))
print(type(string))

#2.3
nummer1=32
nummer2="40"
print(nummer2-nummer1) #Ausgabe: TypeError: unsupported operand type(s) for -: 'str' and 'int'
#Richtige
print(int(nummer2)-nummer1)
