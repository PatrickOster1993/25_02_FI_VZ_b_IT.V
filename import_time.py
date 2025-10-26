import time
zahl = int(input("input"))

while zahl < 100:
    zahl += 1
    print(zahl)
    time.sleep(1)
print(f"Gut! {zahl} wurde erreicht :) ")
