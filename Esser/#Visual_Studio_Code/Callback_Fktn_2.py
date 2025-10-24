def Begrueßung(name):
    print(f"Hallo, liebe(r) {name}, wie geht es dir?")
def WasPassiert(callback):
    name = input("Bitte nennen Sie Ihren Namen: ")
    callback(name)
WasPassiert(Begrueßung)

