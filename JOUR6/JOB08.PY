# Définition de la liste
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la somme
somme_paires = 0

# Parcours de la liste
for nombre in L:
    # Un nombre est pair si le reste de sa division par 2 est 0 (%)
    if nombre % 2 == 0:
        somme_paires += nombre

# Affichage du résultat
print("La somme des valeurs paires de la liste est :", somme_paires)