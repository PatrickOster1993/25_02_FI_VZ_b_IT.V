#def sag_hallo(): #irgendeine Funktion
#    print("Hallo")
#
#
#def mach_was(callback): #diese funktion bekommt einen Parameter diese habe ich callback genannt  print("Ich mach ja was")
#   callback() #innerhalb der mach_was Funktion habe ich Callback() aufgerufen

#mach_was(sag_hallo) #führe es aus
import time

def fertig():
    print("Fertig")

def warte_ruf_auf(callback):
    print(" Warten........")
    time.sleep(5)
    callback()

warte_ruf_auf(fertig)