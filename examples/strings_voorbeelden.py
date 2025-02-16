#Onveranderlijkheid (Immutable):

text = "Hallo"
text[0] = "h"  # Dit geeft een fout

text = "Hallo"
text = "h" + text[1:]  # Maak een nieuwe string met "h" als eerste letter
print(text)            # Output: hallo

text = "Hallo"
text = text.replace("H", "h", 1)  # Alleen de eerste "H" vervangen
print(text)  # Output: hallo


# Strings worden omsloten door enkele (') of dubbele aanhalingstekens ("). 
string1 = 'Hallo'
string2 = "Wereld"

# Veelgebruite stringmethoden zijn len(), lower(), upper(), find(), replace() en strip().

## lengte van een string
text = "Python"
print(len(text))  # 6


## Indexering van een string

text = "Python"
print(text[0])  # P
print(text[-1])  # n

## Slicing

text = "Python"
print(text[0:3])  # Pyt
print(text[:3])  # Pyt
print(text[3:])  # hon


## String samenvoegen

text1 = "Hallo"
text2 = "Wereld"
result = text1 + " " + text2
print(result)  # Hallo Wereld

## Herhalen van een string

text = "Ha"
print(text * 3)  # HaHaHa



s1 = "appel"
s2 = " banaan "

print(s1)  # Output: appel
print(s2)  # Output: banaan
print(s1 + s2)  # Output: appel banaan
print(3 * s1)  # Output: appelappelappel
print(s2 * 3)  # Output: banaan banaan banaan
print(2 * s1 + 2 * s2)  # Output: appelappel banaan banaan


print("string indices")

fun = "party"
print(fun[0])  # Output: 'p'
print(fun[4])  # Output: 'y'
print(fun[2])  # Output: 'r'
print(fun[-2])  # Output: 't'
print(fun[-5])  # Output: 'p'
print(fun[-1])  # Output: 'y'

# The following line will cause an IndexError because the index is out of range.
# Strings in Python are zero-indexed, and 'party' has indices 0 to 4.
# print(fun[5])

print("substrings met stappen")

fun = "party"
print(fun[1:4])  # Output: 'art'
print(fun[1:4:2])  # Output: 'at'
print(fun[:2])  # Output: 'pa'
print(fun[3:])  # Output: 'ty'
print(fun[0::2])  # Output: 'pry'
print(fun[-1::-1])  # Output: 'ytrap'

print("Strings zijn onveranderbaar (immutable)")

original_string = "Hello, world!"

# Attempt to change the first character to 'h'
try:
    original_string[0] = 'h'
except TypeError as e:
    print("Error:", e)

# Shows the original string remains unchanged
print("Original string:", original_string)

# To "modify" the string, you must create a new one
modified_string = 'h' + original_string[1:]
print("Modified string:", modified_string)


fruit = "aaldbei"
# The following line will cause a TypeError:
# fruit[2] = "r"

# Correct approach:
fruit = fruit[:2] + "r" + fruit[3:]
print(fruit)

fruit = "aaldbei"
fruit = fruit.replace("l", "r", 1)  # Only replace the first occurrence
print(fruit)  # Output: aardbei


print("Strings: loopen over string met for-loop")

s1 = "mango"
s2 = "banaan"
for letter in s1:
    if letter in s2:
        print(s1, "en", s2, "bevatten", letter)


print("String functies")


print(len('party'))     # Output: 5
print(len("off you go")) # Output: 10
print(len(""))          # Output: 0
print(len('mango\'s'))  # Output: 7 (The backslash is used to escape the single quote)

print("   \n www.google.com    ".strip())  # Output: 'www.google.com' (whitespace and newline are removed)
print("www.google.com".strip(".com"))     # Output: 'www.google' (.com is removed from the ends)

print("aBcDeF".upper())  # Output: 'ABCDEF'

print("aBcDeF".lower())  # Output: 'abcdef'

quote = 'Let it be, let it be, let it be'
first = quote.find('be')  # Finds the first occurrence of 'be'
print(first)  # Output: index of the first 'be'

# Finds 'be' starting from index 8
print(quote.find("be", 8))  # Output: index of 'be' starting from index 8

# Finds 'be' from index 9 up to index 18
print(quote.find("be", 9, 19))  # Output: index of 'be' from index 9 up to 18, or -1 if not found

