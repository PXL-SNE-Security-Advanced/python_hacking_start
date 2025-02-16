## DataTypes.
##############

# print('dia’s')
# print("Ik zeg: "Hallo"!")


#w = 'dia's'   
# dit is fout, waarom?)
w = "dia's"
print(w)

print(15 / 4)
print(int(15 / 4))
print(float(-17))
print("Ik wil minimum een " + str(16) + " halen.")
# print("Ik wil minimum een " + 16 + " halen.")

## Expressies
#############
print(5**3)
print(5 // 3)

print(6 - 10 / 2 + 9)
print((6 - 10) / 2 + 9)
print(15 / 6 * 2) 
print(10 - 6 % 4 / 2)

## String expressies
####################
text = "Hallo"
#text[0] = "h" # Dit geeft een fout

text = "Hallo"
text = "h" + text[1:]  # Maak een nieuwe string met "h" als eerste letter
print(text)            # Output: hallo

text = "Hallo"
text = text.replace("H", "h", 1)  # Alleen de eerste "H" vervangen
print(text)  # Output: hallo

## String methoden
##################
text = "Python"
print(text[0]) # P
print(text[-1]) # n

print(text[0:3])# Pyt
print(text[:3]) # Pyt
print(text[3:]) # hon

## String formatting
####################

