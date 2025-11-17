def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# Beispiel: die ersten 10 Zahlen ausgeben
for i in range(10):
    print(fibonacci(i))

print("==============================================================================================================================")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci (n - 2)
print (fibonacci(3))


print("==============================================================================================================================")



def biggest_value(liste, n):
    
    if n == 1:
        return liste[0]
 
    max_rest = biggest_value(liste, n-1)

    print("max_rest =", max_rest)
    print("liste[n-1]:", liste[n-1])
    print("n =",n)
    print("################################################")

    if liste[n-1] > max_rest:
        return liste[n-1]
    else:
        return max_rest
    

    


meine_liste = [5, 8, 99, 3, 1, 43, 0]
n = len(meine_liste)
 
print(biggest_value(meine_liste, n))


print("=============================================================================================================================")


