# Lijst aanmaken
empty_list = []  # Lege lijst
numbers = [1, 2, 3, 4, 5]  # Lijst met getallen
mixed = [1, "apple", 3.5, True]  # Gemengde lijst

# Toegang tot elementen
# Indexing (start vanaf 0)
my_list = [10, 20, 30, 40]
print(my_list[0])  # 10
print(my_list[-1])  # 40 (laatste element)


# slicing

print(my_list[1:3])  # [20, 30]
print(my_list[:2])  # [10, 20] (eerste twee elementen)


# elementen toevoegen

# append(): Voeg een element toe aan het einde
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
# insert(): Voeg een element toe op een specifieke positie.
my_list.insert(1, 10)
print(my_list)  # [1, 10, 2, 3]


# Elementen verwijderen

# remove(): Verwijder het eerste voorkomen van een waarde
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2]


# pop(): Verwijder en retourneer een element op een specifieke index (standaard het laatste)
my_list = [1, 2, 3]
my_list.pop()
print(my_list)  # [1, 2]


#Elementen aanpassen
#Wijzig een element door directe toewijzing:
my_list = [1, 2, 3]
my_list[1] = 10
print(my_list)  # [1, 10, 3]

#Lengte van een lijst
print(len(my_list))  # Geeft het aantal elementen in de lijst.


#Lijst samenvoegen
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4]


#Controleer op aanwezigheid
print(3 in my_list)  # True als 3 in de lijst zit, anders False.

# Hoe vaak komt een element voor in de lijst

fruits = ['orange', 'apple', 'banana', 'apple']
print(fruits.count('apple'))




# Itereren door een lijst
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)


# voorbeeld lijstgebruik
# Een lijst maken
fruits = ["apple", "banana", "cherry"]

# Elementen toevoegen en verwijderen
fruits.append("orange")
fruits.remove("banana")

# Itereren door de lijst
for fruit in fruits:
    print(fruit)

# Output: apple, cherry, orange



#Lijst als parameter meegeven in een functie
def wijziglist(mijn_list, index):
	if index >= 0 and index < len(mijn_list):
            mijn_list[index] = "FRUIT!"

def main():
	fruitlist = ["appel", "banaan", "kers", "doerian"]
	te_wijzigen = 2
	wijziglist(fruitlist, te_wijzigen)
	print(fruitlist)

if __name__ == '__main__':
    main()

# Output:
# ['appel', 'banaan', 'FRUIT!', 'doerian']



#Lijst maken vanuit een string.


colors = "red,green,yellow"
color_list = colors.split(",")
print(color_list)
print(color_list[1])


Output:
['red', 'green', 'yellow']
green



fruitlist = ["appel", "banaan", "kers", "mango"]  # appel heeft positie 0, mango 3
print("Aantal elementen in fruitlist:", len(fruitlist))  # len(): aantal elementen (lengte)

print ("elmeneten fruite:")

for element in fruitlist:
    print(element)
print(fruitlist[2])  # print enkel het element op positie 2 (startend vanaf 0!!!)


print ("nummers van een lijst:")


numberlist = [314, 315, 642, 246, 129, 999]
for number in numberlist:
    print(number)
print(numberlist[3])  # print enkel het element op positie 3 (startend vanaf 0!!!)


print ("aantal elementen van een specifieek waarde in eenlijst:")
fruits = ['orange', 'apple', 'banana', 'apple']
print(fruits.count('apple'))


print ("een element verwijderen uit een lijst")

fruits = ['orange', 'apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)
# fruits.remove('kiwi') ## geeft een error - list.remove(x): x not in list


print ("list.index(x, start, end): op welke positie staat het eerste element gelijk aan x? (geeft ValueError als element niet bestaat)​")
fruits = ['orange', 'apple', 'banana', 'apple']
print(fruits.index('apple'))


print ("zoek pas vanaf positie 2 in lijst")
print(fruits.index('apple', 2)) # zoek pas vanaf positie 2 in lijst


print ("splitten van een lijst:")

colors = "red,green,yellow"

color_list = colors.split(",")
print(color_list)

print(color_list[1])


print ("List maken via een casting:")
numlist = list(range(1, 11))
print(numlist)


