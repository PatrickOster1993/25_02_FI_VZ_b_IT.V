
while True:
    Preis = input("Gib den Preis an")
    try:
        float_value = float(Preis)
        print("Entered Number as a float.",float_value)
        break # Exit the loop if the conversion was successful
    except ValueError:
        print("Falsche Eingabe, bitte geben Sie eine Zahl ein.")
        # The Loop continues to promt for valid input


 
 