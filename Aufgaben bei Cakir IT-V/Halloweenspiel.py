from random import randint
import playsound3
from time import sleep
 
# --- Sound initialisieren ---
playsound3.playsound(r"C:\Users\IT-User\Downloads\Cakir II.wav")

 
 
 
print("Willkommen bei THE SAW, dem tödlichen Zahlenrätsel \U0001F60A")
print("\n Du hast drei Versuche, richtige Zahl zwischen 1 und 10 zu erraten")
print("Wenn du die Prüfung nicht schaffst, wirst du eliminiert \U0001F608 ")
 
# Intro-Sound (blockierend, wird einmal abgespielt)
pygame.mixer.music.load(r"C:\Users\IT-User\Downloads\Cakir II.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(0.1)
 
# Hintergrundmusik starten (läuft endlos im Hintergrund)
pygame.mixer.music.load(r"C:\Users\IT-User\Downloads\saw-theme-1-made-with-Voicemod.mp3")
pygame.mixer.music.play(-1)  # -1 = Endlosschleife
 
wrong_answer = pygame.mixer.Sound(r"C:\Users\IT-User\Downloads\SAW.wav")
 
random_number=randint(1,10)
attempts=2
       
while attempts>0:
    input_value=input(f"Ich möchte ein Spiel spielen, gebe eine Zahl zwischen 1 und 10 ein, du hast jetzt {attempts} Versuche frei \U0001F60A")
 
    if input_value.isdigit():
        input_value=int(input_value)# if 1<= input_value and input_value <=10:
        if 1<= input_value <=10:
            if input_value==random_number:
                print("\U0001F60A \U0001F60A \U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A")
                print(" Du hast heute gewonnen, ich hoffe du lernst aus deinen Fehlern du hast dir dein Leben verdient")
                print("\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A\U0001F60A")
                break
            else:
                attempts-=1
               
                if input_value<random_number:
                    wrong_answer.play()
                    print(f"Die gesuchte Zahl ist höher")
                   
                elif input_value>random_number:
                    wrong_answer.play()
                    print(f"Die gesuchte Zahl ist kleiner")
                   
               
               
 
                if attempts>0:
                    print(f" Falsch geraten, versuche es nochmal \U0001F480 ")
                else:
                    print("______________________________________________________________________")
                    print("\n Du hast alle deine Chancen verspielt")
                    print(f" Da war dein finales Spiel. Für dich heißt es GAME OVER \U0001F480")
                    print(f"Die gesuchte Zahl war {random_number} \U0001F480")
                    print("______________________________________________________________________")
                    wrong_answer.play()
        else:
            print(f"Die Spielregeln lauten Zahlen zwischen 1 und 10 eingeben")
            wrong_answer.play()
    else:
        print("Sonst hast du keine Probleme oder??? Sieht das aus wie eine Zahl???")
        wrong_answer.play()
        attempts-=1
 
     
print("Vielen Dank, dass du mitgespielt hast")