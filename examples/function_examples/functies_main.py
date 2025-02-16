import math
#from math import pow, sqrt

def bereken(getal1, getal2):
    if getal1 > getal2:
        resultaat = getal1 * 2
    else:
        resultaat = getal2 * 3
    return resultaat

def main():
    print("Hello world!")
    print("functie voorbeeld - berekenen")

    a = 5
    b = 7
    c = bereken(a, b)

    print(c + 4)

    x = 20
    y = 15
    z = bereken(x, y)
    print(z)

    print("functie voorbeeld - math")
    x = math.pow(2, 5)
    y = math.sqrt(4)
    #x = pow(2, 5)
    #y = sqrt(4)
    
    print(x, y)


if __name__ == "__main__":
    main()
