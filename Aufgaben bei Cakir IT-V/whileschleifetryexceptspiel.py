import random
print("Ich möchte ein Spiel spielem :D")
print("Gebe eine Zahl zwische 1 und 10 ein: ")
try:
    input_value=int(input())
    num_attempts=1
    random_number=random.randint(1,10)
    while input_value!= random_number:
        print("\n Hahaha Pech gehabt, du hast noch einen versuch")
        print("Also gebe nochmal eine Ganze Zahl zwischen 1 und 10 ein")
        try:
            input_value=int(input())
            num_attempts+=1
        except ValueError:
            print("Alter das war keine Gültige Zahl")
    print(f"Du gewinnst nach {num_attempts} versuchen")        
except ValueError:
    print("Egal wie du wirst eine gültige Zahl eingeben")