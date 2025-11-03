from playsound3 import playsound
import time
def countdown(a=11):
    while a>1:
        a-=1
        print(f"noch {a} Sekunden")
        time.sleep(1)
    else:
        playsound("tada.mp3")
        print("Der Countdown ist beendet!!!")

countdown()


