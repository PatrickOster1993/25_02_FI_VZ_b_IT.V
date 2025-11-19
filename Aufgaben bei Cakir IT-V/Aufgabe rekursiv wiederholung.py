# Übung 1: Grundlegende rekursive Funktionen
############################################
# a) power(a, b): Berechnet a^b
def power(a, b):
    # Abbruchbedingung (anhand Skizze unten ermittelt (*)):
    if b == 0:
        return 1
    # rekursiver Aufruf:
    return a * power(a, b - 1)
    # Tiefenstruktur bei a = 2 und b = 3 (*):
        ## 1. Ebene
        ## return (2 * power(2, 2))
            ## 2. Ebene
            ## return(2 * 2 * return(power(2, 1)))
                ## 3. Ebene
                ## return(2 * 2 * 2 * return(power(2, 0)))
                    ## 4. Ebene
                    ## return (2 * 2 * 2 * 1) --> gibt 1 an Ebene 3 zurück
                ## 3. Ebene -> gibt 2 * 1 an Ebene 2 zurück
            ## 2. Ebene --> gibt 2 * 2 * 1 an Ebene 1 zurück 
        ## 1. Ebene --> return 2 * 2 * 2 * 1 an main()-Funktion (**) --> gibt 2 * 2 * 2 * 1 an main() zurück


# (**)
ergebnis = power(2, 3)
print(ergebnis)
# Wie wir das lösen wollen:
## 2 bleibt immer gleich bei jedem rekursiven Aufruf!
## Lösung: 2 * 2 * 2 (entsprich: 2^3)
# b) reverse_string(text): dreht Text rekursiv um (Beispiel: hallo -> ollah)
def reverse_string(text):
    # Abbruchbedingung:
    if len(text) == 1:
        return text
    # Rekursiver Teil:
    erstes_zeichen = text[0]
    rest = text[1:]
    
    return reverse_string(rest) + erstes_zeichen
ergebnis = reverse_string("hallo")
## Was ist rest + erstes_zeichen?
## allo h
### llo a h
#### lo l a h
##### o l l a h --> zurückgeliefert
print(ergebnis)
# main()
ergebnis = reverse_string("hai")
## 1. Ebene
## return (reverse_string(ai) + h)
    ## 2. Ebene
    ## return (return (reverse_string(i) + a) + h)
        ## 3. Ebene
        ## (return (return (return i) + a) + h) --> "iah"
        ## 3. Ebene gibt "i" an 2. Ebene
    ## 2. Ebene gibt "ia" an 1. Ebene
## 1. Ebene gibt "ia" + 1. Zeichen ("h") = "iah" an main() zurück
print(ergebnis)
# c) count_x(text): zählt, wie oft "x" in Text vorkommt
def count_x(text):
    # Abbruchbedingung:
    if len(text) == 0:
        return 0
    
    else:
        # Rekursiver Teil:
        erstes_zeichen = text[0]
        rest = text[1:]
        counter = 0
        if erstes_zeichen == "x":
            counter = 1
        # print(counter) -> für "Debugging + Zurückverfolgung"
        return counter + count_x(rest)
# Beispiel "hexe":
# return 0 + count_x(exe)
## return 0 + 0 + count_(xe)
### return 0 + 0 + 1 + count_(e)
#### return 0 + 0 + 1 + 0 + count()
##### return 0 + 0 + 1 + 0 + 0 
# -> oberste Ebene erhält (0 + 0 + 1 + 0 + 0) als Ergebnis -> entspricht 1

# main():
ergebnis = count_x("hexe")
print(ergebnis)


print("=======================================================")




def sum_digits(n):
        if n<10:
            return n
    
        letzte_ziffer=n % 10
        rest_der_zahl =n // 10

        return letzte_ziffer + sum_digits(rest_der_zahl)

ergebnis=sum_digits(54321)

print(ergebnis)

print("======================================================================")



def count_vowels(text):
    if len(text)==0:
        return 0
    
    count=0
    
    rest_des_textes= text[1:]
    if text[0]== "a" or text[0]=="e" or  text[0]== "i" or text[0]== "o" or text[0]== "u" :
        count=1

    return count + count_vowels(rest_des_textes)

ergebnis= count_vowels("Vogel")

print(ergebnis)




print("=======================================")



def count_vowels(text):

    # Abbruchbedingung

    if text == "":

        return 0
 
    vowels = "aeiouAEIOU"  # Groß- und Kleinschreibung berücksichtigen
 
    # Prüfen, ob das erste Zeichen ein Vokal ist

    first_is_vowel = 1 if text[0] in vowels else 0
 
    # Rekursiver Aufruf mit dem Rest des Strings

    return first_is_vowel + count_vowels(text[1:])

 
print(count_vowels("Vogel"))




print("===================================================================================")



def is_palindrome(text):
    if len(text)== 0:
        return ("Ist ein Palindrome")
    

   
    
    

    if text[0] != text[-1]:
        return print("Ist kein Palindrom")
    return is_palindrome(text[1:-1])

ergebnis=is_palindrome("lagerregal")

print(ergebnis)
   


