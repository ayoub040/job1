# Définition de la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# On initialise le maximum et le minimum avec le premier élément
maximum = L[0]
minimum = L[0]

# Parcours des éléments de la liste
for nombre in L:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre

print("Valeur maximale :", maximum)
print("Valeur minimale :", minimum)