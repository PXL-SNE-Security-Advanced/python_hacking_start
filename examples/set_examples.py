# Elementen toevoegen:
mijn_set = {1, 2, 3}
mijn_set.add(4)
print(mijn_set)  # Output: {1, 2, 3, 4}

# Elementen verwijderen:
# remove(): Verwijdert een element, geeft een fout als het element niet bestaat.
# discard(): Verwijdert een element, geeft geen fout als het element niet bestaat.
mijn_set = {1, 2, 3, 4}
mijn_set.remove(3)
print(mijn_set)  # Output: {1, 2, 4}
mijn_set.discard(5)  # Geen fout als 5 niet in de set staat

# Unie:
# Combineert alle unieke elementen uit twee sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Doorsnede:
# Vindt elementen die in beide sets voorkomen.
print(set1 & set2)  # Output: {3}

# Verschil:
# Vindt elementen die in de ene set staan maar niet in de andere.
print(set1 - set2)  # Output: {1, 2}

