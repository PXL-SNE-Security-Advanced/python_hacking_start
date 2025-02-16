import random

def main():
    # genereer random float >= 0 en < 1
    a = random.random()

    # genereer random float >= ondergrens en <= bovengrens
    ondergrens = 10
    bovengrens = 100
    b = random.randrange(ondergrens, bovengrens)

    print(a, b)

if __name__ == '__main__':
    main()
