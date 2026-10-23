# Définition de la liste
L = [8, 24, 48, 2, 16]

# Initialisation du compteur
compteur = 0

# Parcours de la liste
for nombre in L:
    # Un nombre est multiple de 3 si le reste de sa division par 3 est 0 (%)
    if nombre % 3 == 0:
        compteur += 1

# Affichage du résultat
print("Le nombre de multiples de 3 dans la liste est :", compteur)