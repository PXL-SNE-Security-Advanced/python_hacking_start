x = 41

if x % 7 == 0:
    # Hier begint een genest blok code
    if x % 11 == 0:
        print(x, "is deelbaar door 7 en 11.")
    else:
        print(x, "is deelbaar door 7, maar niet door 11.")
    # Hier eindigt een genest blok code
elif x % 11 == 0:
    print(x, "is deelbaar door 11, maar niet door 7.")
else:
    print(x, "is niet deelbaar door 7 of 11.")
